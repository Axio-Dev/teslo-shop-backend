from django.urls import path
from .views import LoginAPIView, RegisterAPIView, CheckUserStatusAPIView, LogoutAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("check-status/", CheckUserStatusAPIView.as_view(), name="user-status"),
]
