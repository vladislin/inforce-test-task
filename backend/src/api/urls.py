from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    CreateRestaurantAPIView,
    CreateEmployeeAPIView,
    UploadMenuAPIView,
    CurrentDayMenuList,
    VoteAPIView,
)


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create-restaurant/', CreateRestaurantAPIView.as_view(), name="create-restaurant"),
    path('create-employee/', CreateEmployeeAPIView.as_view(), name="create-employee"),
    path('upload-menu/', UploadMenuAPIView.as_view(), name="upload-menu"),
    path('menu-list/', CurrentDayMenuList.as_view(), name="menu-list"),
    path('vote/<int:menu_id>/', VoteAPIView.as_view(), name="new-vote"),
]

