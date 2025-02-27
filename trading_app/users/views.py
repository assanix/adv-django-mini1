from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model

from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, UserProfileSerializer
from .permissions import IsAdminUser, IsTraderUser, IsSalesRepresentative, IsClient



User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return user


class TraderDashboardView(generics.GenericAPIView):
    permission_classes = [IsTraderUser]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Trader Dashboard: Access granted."}, status=status.HTTP_200_OK)

class SalesDashboardView(generics.GenericAPIView):
    permission_classes = [IsSalesRepresentative]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Sales Dashboard: Welcome to your workspace."}, status=status.HTTP_200_OK)

class CustomerDashboardView(generics.GenericAPIView):
    permission_classes = [IsClient]

    def get(self, request, *args, **kwargs):
        return Response({"message": "Customer Dashboard: Explore your account."}, status=status.HTTP_200_OK)

class UserProfileUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        return user