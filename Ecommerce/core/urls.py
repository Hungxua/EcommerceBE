from django.urls import  path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', views.ProductCategoryViewSet, basename='category')
router.register('inventories', views.ProductInventoryViewSet, basename='inventory')
router.register('discounts', views.DiscountViewSet, basename='discount')
router.register('products', views.ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls))
]