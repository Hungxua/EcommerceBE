from django.urls import  path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', views.ProductCategoryViewSet, basename='category')
router.register('inventories', views.ProductInventoryViewSet, basename='inventory')
router.register('discounts', views.DiscountViewSet, basename='discount')
router.register('products', views.ProductViewSet, basename='product')
router.register('shopping-session', views.ShoppingSessionViewSet, basename='shopping-session')
router.register('order-detail', views.OrderDetailViewSet, basename='order-detail')
router.register('user', views.UserViewSet, basename='user')


urlpatterns = [
    path('', include(router.urls))
]