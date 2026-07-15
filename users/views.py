from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer 


class LoginAPIView(APIView):

    def post(self, request):

        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(
            email=email,
            password=password
        )

        if user is None:
            return Response(
                {
                    "error": "Invalid credentials"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        refresh = RefreshToken.for_user(user)

        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })

class RegisterAPIView(APIView):

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.save()

            refresh = RefreshToken.for_user(user)

            return Response({
                "user": serializer.data,
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=status.HTTP_201_CREATED
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
