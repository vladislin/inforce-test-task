from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import (
    Restaurant,
    Menu,
    Employee,
    User
)


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name', 'address']
        model = Restaurant


class UploadMenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = [
            'restaurant',
            'file',
            'uploaded_by'
        ]

    def create(self, validated_data):
        menu = Menu(
            file=validated_data['file'],
            restaurant=validated_data['restaurant'],
            uploaded_by=validated_data['uploaded_by']
        )
        menu.save()
        return menu


class MenuListSerializer(serializers.ModelSerializer):

    restaurant = serializers.CharField(read_only=True)

    class Meta:
        model = Menu
        fields = '__all__'


class CreateEmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self, **kwargs):
        instance = super().save(
            password=make_password(self.validated_data['password'])
        )
        Employee.objects.create(user=instance)
        return instance


class ResultMenuListSerializer(serializers.ModelSerializer):

    restaurant = serializers.CharField(read_only=True)

    class Meta:
        model = Menu
        fields = [
            'id',
            'file',
            'restaurant',
            'votes',
            'created_at'
        ]
