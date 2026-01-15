from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ratelimit import limits
from rest_framework_simplejwt.tokens import RefreshToken
from .models import SmsUser,LoginToken
from django.http import JsonResponse

FIFTEEN_MINUTES = 900
API_KEY = "MY_SUPER_SECRET_KEY"

@api_view(["POST"])
@limits(calls=15, period=FIFTEEN_MINUTES)
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)

    if not user:
        return Response({
            "responseCode": 4,
            "responseMessage": "Invalid username or password",
            "data": [],
            "dataCount": 0,
        }, status=status.HTTP_401_UNAUTHORIZED)
    
    profile_data = {
        "id": user.id,
        "username": user.username,
        "role": user.role,
    }

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)

    # Store token (important for middleware validation)
    LoginToken.objects.update_or_create(
        user=user,
        defaults={"token": access_token}
    )

    return Response({
        "responseCode": 0,
        "responseMessage": "Logged in successfully",
        "data": {
            "access": access_token,
            "refresh": str(refresh),
            "profile": profile_data,
        },
        "dataCount": 2,
    })

def jwt_request(payload: dict):
    refresh = RefreshToken()
    for key, value in payload.items():
        refresh[key] = value
    return {
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    }


@api_view(["GET"])
def get_jwt_token(request):
    api_key = request.query_params.get("api_key")
    if api_key != API_KEY:
        return Response({
            "responseCode": 4,
            "responseMessage": "Invalid API key",
            "data": [],
            "dataCount": 0,
        }, status=status.HTTP_401_UNAUTHORIZED)


    tokens = jwt_request({"scope": "public", "issued_for": "frontend"})
    return Response({
        "responseCode": 0,
        "responseMessage": "success",
        "data": tokens,
        "dataCount": len(tokens),
    })

@api_view(["GET"])
def get_jwt_token_by_client_id(request):
    client_id = request.query_params.get("client_id")
    if not client_id:
        return Response({
            "responseCode": 4,
            "responseMessage": "Missing client_id",
            "data": [],
            "dataCount": 0,
        }, status=status.HTTP_400_BAD_REQUEST)

    tokens = jwt_request({"client_id": client_id})
    return Response({
        "responseCode": 0,
        "responseMessage": "success",
        "data": tokens,
        "dataCount": len(tokens),
    })
@api_view(["GET"])
def users_client_view(request):
    users = SmsUser.objects.all().order_by("-created_at")

    users_list = []
    for u in users:
        users_list.append({
            "id": u.id,
            "username": u.username,
            "email": u.email,
            "role": u.role,
            "created_at": u.created_at.strftime("%Y-%m-%d %H:%M:%S")
        })

    return JsonResponse(users_list, safe=False)