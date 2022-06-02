from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics, status, permissions
from .models import ProductCategory, ProductInventory, Product, Discount
from .serializers import (ProductSerializer, ProductCategorySerializer,
ProductInventorySerializer, UserSerializer,DiscountSerializer )

from rest_framework.decorators import action
from rest_framework.response import Response



class ProductCategoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    @action(methods=['GET'],detail=True, url_path='get-products')
    def get_products(self, request, pk):
        category = ProductCategory.objects.get(pk=pk)

        if category is not None:
            products = category.product_set.all()
            return Response(ProductSerializer(products, many=True).data,
                            status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class ProductInventoryViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer


class DiscountViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Discount.objects.filter(active = True)
    serializer_class = DiscountSerializer


class ProductViewSet(viewsets.ViewSet, generics.ListAPIView, generics.CreateAPIView,
                     generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(methods=['GET'], detail=True, url_path='get-inventory')
    def get_inventory(self, request, pk):
        product = Product.objects.get(pk = pk)
        if product is not None:
            inventory = product.inventory
            return Response(ProductInventorySerializer(inventory, many = False).data,
                            status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

