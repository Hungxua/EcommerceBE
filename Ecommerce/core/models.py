from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    telephone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None)

    def __str__(self):
        return self.name


class ProductInventory(models.Model):
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None)


class Discount(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    discount_percent = models.FloatField(default=0)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    stockKeepingUnit = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    inventory = models.ForeignKey(ProductInventory, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=None)

    def __str__(self):
        return self.name


class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    addressLine = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    telephone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)


class UserPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paymentType = models.CharField(max_length=50)
    provider = models.CharField(max_length=50)
    accountNo = models.CharField(max_length=15)
    expiry = models.DateTimeField(default=None)


class ShoppingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    session = models.ForeignKey(ShoppingSession, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class PaymentDetail(models.Model):
    amount = models.IntegerField(default=0)
    provider = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class OrderDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    payment = models.ForeignKey(PaymentDetail, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class OrderItems(models.Model):
    order = models.ForeignKey(OrderDetail, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
