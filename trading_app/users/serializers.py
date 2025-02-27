from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user model with basic fields."""
    
    class Meta:
        model = User
        fields = ["id", "username", "email", "role", "profile_image"]

class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration."""
    
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ["username", "email", "password", "role", "profile_image"]

    def create(self, validated_data):
        """Creates a new user with hashed password."""
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            role=validated_data.get("role", "customer"),
            profile_image=validated_data.get("profile_image"),
        )

class LoginSerializer(serializers.Serializer):
    """Serializer for user authentication."""
    
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={"input_type": "password"})

    def validate(self, data):
        """Validates user credentials and generates tokens."""
        user = User.objects.filter(username=data["username"]).first()
        if user and user.check_password(data["password"]):
            refresh = RefreshToken.for_user(user)
            return {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data,
            }
        raise serializers.ValidationError("Invalid credentials")

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for updating user profile."""
    
    profile_image = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = ["id", "username", "email", "role", "profile_image"]

    def update(self, instance, validated_data):
        """Updates user profile fields."""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
