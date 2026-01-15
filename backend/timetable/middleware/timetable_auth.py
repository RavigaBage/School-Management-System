from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from .models import LoginToken, Teacher, TeacherClassSubject

class TimetableMiddleware(MiddlewareMixin):

    def process_request(self, request):

        auth = request.headers.get("Authorization")

        if not auth or not auth.startswith("Bearer "):
            return JsonResponse(
                {"error": "Authentication token required"},
                status=401
            )

        token = auth.split(" ")[1]

        try:
            login = LoginToken.objects.select_related("user").get(token=token)
        except LoginToken.DoesNotExist:
            return JsonResponse(
                {"error": "Invalid or expired token"},
                status=401
            )

        user = login.user

        # Attach identity
        request.user = user
        request.user_name = user.get_full_name()
        request.user_role = user.role

        # Teacher-specific resolution
        if user.role == "teacher":
            teacher = Teacher.objects.get(user=user)

            assignments = TeacherClassSubject.objects.filter(
                teacher=teacher
            )

            request.allowed_classes = list(
                assignments.values_list("classroom_id", flat=True)
            )

            request.allowed_subjects = list(
                assignments.values_list("subject_id", flat=True)
            )

            request.allowed_operations = {
                "view": True,
                "add": True,
                "edit": True,
                "delete": False
            }

        return None
