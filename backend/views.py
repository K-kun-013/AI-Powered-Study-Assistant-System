from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .serializers import UserRegistrationSerializer, UserLoginSerializer, JWTSerializer
from django.contrib.auth.models import User

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=201)
        return Response(serializer.errors, status=400)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                refresh = RefreshToken.for_user(user)
                jwt_serializer = JWTSerializer({
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                })
                return Response(jwt_serializer.data)
            return Response({'error': 'Invalid credentials'}, status=401)
        return Response(serializer.errors, status=400)

class RoleBasedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.role == 'admin':
            return Response({'message': 'Hello, Admin!'}, status=200)
        elif request.user.role == 'user':
            return Response({'message': 'Hello, User!'}, status=200)
        return Response({'error': 'Role not recognized'}, status=403)