from django.urls import path
from .views import login_view,get_jwt_token,users_client_view

urlpatterns = [
    path("login/", login_view, name="login"),
    path("get_jwt_token_by_api_key/", get_jwt_token, name="get_jwt_token_by_api_key"),
    path("get_users/", users_client_view, name="get_user")
]
