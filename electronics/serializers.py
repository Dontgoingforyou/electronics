from rest_framework import serializers
from electronics.models import NetworkNode
from django.contrib.auth.models import User


class NetworkNodeSerializer(serializers.ModelSerializer):
    supplier_name = serializers.CharField(source="supplier.name", read_only=True)

    class Meta:
        model = NetworkNode
        fields = [
            "id", "name", "email", "country", "city", "street", "house_number",
            "supplier", "supplier_name", "debt", "level", "created_at"
        ]
        read_only_fields = ["debt", "level", "created_at"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
