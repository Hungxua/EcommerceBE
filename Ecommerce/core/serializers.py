from rest_framework.serializers import ModelSerializer
from .models import ProductCategory, ProductInventory, Product, User, Discount


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

