from rest_framework.serializers import ModelSerializer
from .models import (ProductCategory, ProductInventory, Product, User, Discount,
                     ShoppingSession,CartItem,OrderItems,OrderDetail,PaymentDetail,
                     UserPayment,UserAddress)


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name',
                  'telephone', 'created_at', 'modified_at']


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'desc', 'created_at', 'modified_at', 'deleted_at']


class ProductInventorySerializer(ModelSerializer):
    class Meta:
        model = ProductInventory
        fields = ['id', 'quantity', 'created_at', 'modified_at', 'deleted_at']


class DiscountSerializer(ModelSerializer):
    class Meta:
        model = Discount
        fields = ['id', 'name', 'desc', 'discount_percent',
                  'active', 'created_at', 'modified_at', 'deleted_at']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'desc', 'stockKeepingUnit', 'category_id',
                  'inventory_id', 'price', 'discount_id', 'created_at', 'modified_at', 'deleted_at']


class ShoppingSessionSerializer(ModelSerializer):
    class Meta:
        model = ShoppingSession
        fields = ['id', 'user_id', 'total', 'created_at', 'modified_at']


class CartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'session_id', 'product_id', 'quantity', 'created_at','modified_at']


class OrderItemsSerializer(ModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['id', 'order_id', 'product_id', 'quantity', 'created_at', 'modified_at']


class OrderDetailSerializer(ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ['id', 'user_id', 'total', 'payment_id', 'created_at', 'modified_at']


class PaymentDetailSerializer(ModelSerializer):
    class Meta:
        model = PaymentDetail
        fields = ['id', 'order_id', 'product_id', 'quantity', 'created_at', 'modified_at']


class UserPaymentSerializer(ModelSerializer):
    class Meta:
        model = UserPayment
        fields = ['id', 'user_id', 'paymentType', 'provider', 'accountNo', 'expiry']


class UserAddressSerializer(ModelSerializer):
    class Meta:
        model = UserAddress
        fields = ['id', 'user_id', 'addressLine', 'city', 'postal_code', 'country',
                  'telephone', 'mobile']