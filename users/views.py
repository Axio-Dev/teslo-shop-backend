from django.contrib.auth import authenticate, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    refresh["role"] = user.role
    refresh["email"] = user.email
    refresh["name"] = f"{user.first_name} {user.last_name}".strip()

    access = refresh.access_token
    access["role"] = user.role
    access["email"] = user.email

    return {"token": str(access)}


class LoginAPIView(APIView):
    def post(self, request):

        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is None:
            return Response(
                {"error": "Invalid credentials, check your email or password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        tokens = get_tokens_for_user(user)

        return Response(
            {
                "user": {
                    "id": str(user.id),
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role,
                    "is_active": user.is_active,
                },
                **tokens,
            },
            status=status.HTTP_200_OK,
        )


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(
            {"message": "user logout successfully"}, status=status.HTTP_200_OK
        )


class RegisterAPIView(APIView):
    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            tokens = get_tokens_for_user(user)

            return Response(
                {
                    "user": {
                        "id": str(user.id),
                        "email": user.email,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "role": user.role,
                        "is_active": user.is_active,
                    },
                    **tokens,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckUserStatusAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tokens = get_tokens_for_user(request.user)

        return Response(
            {
                "user": {
                    "id": request.user.id,
                    "email": request.user.email,
                    "first_name": request.user.first_name,
                    "last_name": request.user.last_name,
                    "role": request.user.role,
                },
                "token": tokens["token"],
            }
        )
