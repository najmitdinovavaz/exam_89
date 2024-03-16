from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.views import RegisterCreateAPIView, CategoryListAPIView, ProductListAPIView, ProductUpdateDestroyAPIView

# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register()

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('products/', ProductUpdateDestroyAPIView.as_view(), name='product_list'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterCreateAPIView.as_view(), name='register'),
    path('categories/', CategoryListAPIView.as_view(), name='category'),
    path('search/', ProductListAPIView.as_view(), name='product')
]
