from django.conf import settings
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Menu, Employee, Vote
from .serializers import (
    RestaurantSerializer,
    UploadMenuSerializer,
    MenuListSerializer,
    CreateEmployeeSerializer, ResultMenuListSerializer,
)


class CreateRestaurantAPIView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = RestaurantSerializer

    def perform_create(self, serializer):
        serializer.save()


class UploadMenuAPIView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UploadMenuSerializer

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)


class CreateEmployeeAPIView(CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = CreateEmployeeSerializer

    def perform_create(self, serializer):
        serializer.save()


class CurrentDayMenuList(APIView):

    def get(self, request):
        qs = Menu.objects.filter(created_at=settings.CURRENT_DATE)
        serializer = MenuListSerializer(qs, many=True)
        res = {"msg": 'success', "data": serializer.data, "success": True}
        return Response(data=res, status=status.HTTP_200_OK)


class VoteAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, menu_id):
        username = request.user.username

        employee = Employee.objects.get(user__username=username)
        menu = Menu.objects.get(id=menu_id)

        if Vote.objects.filter(
                employee=employee,
                voted_at__date=settings.CURRENT_DATE,
                menu__id=menu_id).exists():
            res = {"msg": 'You already voted!', "data": None, "success": False}
            return Response(data=res, status=status.HTTP_200_OK)
        else:
            new_vote = Vote.objects.create(
                employee=employee,
                menu=menu
            )
            menu.votes += 1
            menu.save()

            qs = Menu.objects.filter(created_at=settings.CURRENT_DATE)
            serializer = ResultMenuListSerializer(qs, many=True)
            res = {
                "msg": 'You voted successfully!',
                "data": serializer.data,
                "success": True}
            return Response(data=res, status=status.HTTP_200_OK)
