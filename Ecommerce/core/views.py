from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, generics, status, permissions
from .models import (ProductCategory, ProductInventory, Product, Discount,
                     UserAddress,UserPayment,PaymentDetail,OrderDetail,
                     OrderItems,CartItem,ShoppingSession,User)
from .serializers import (ProductSerializer, ProductCategorySerializer,ProductInventorySerializer,
                          UserSerializer,DiscountSerializer,CartItemSerializer,OrderItemsSerializer,
                          OrderDetailSerializer,UserAddressSerializer,UserPaymentSerializer,
                          PaymentDetailSerializer,ShoppingSessionSerializer)

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


class ShoppingSessionViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = ShoppingSession.objects.all()
    serializer_class = ShoppingSessionSerializer


class OrderDetailViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer


class UserViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['GET'], detail=True, url_path= 'get-address')
    def get_address(self, request, pk):
        user = User.objects.get(pk = pk)

        if user is not None:
            address = user.useraddress_set.all()
            return Response(UserAddressSerializer(address, many=True).data,
                            status= status.HTTP_200_OK)
        return Response(status = status.HTTP_404_NOT_FOUND)


    @action(methods=['GET'], detail=True, url_path='get-payments')
    def get_payments(self, request, pk):
        user = request.user

        if user is not None:
            payments = user.userpayment_set.all()
            return Response(UserPaymentSerializer(payments, many=True).data,
                            status = status.HTTP_200_OK)

        return Response(status = status.HTTP_404_NOT_FOUND)

    @action(methods=['GET'], detail=True, url_path='cart-items')
    def get_cart(self, request, pk):
        user = request.user

        if user is not None:
            shoppingSession = list(user.shoppingsession_set.all())
            print(shoppingSession)
            if shoppingSession is not None:
                carts = shoppingSession[0].cartitem_set.all()

                return Response(CartItemSerializer(carts, many=True).data,
                                status = status.HTTP_200_OK)


        return Response(status = status.HTTP_404_NOT_FOUND)
