from django.contrib import admin
from .models import (User, ProductCategory, ProductInventory, Discount, Product,
                     OrderDetail,PaymentDetail,UserPayment,UserAddress,
                     OrderItems,CartItem,ShoppingSession)

admin.site.register(User)
admin.site.register(ProductCategory)
admin.site.register(ProductInventory)
admin.site.register(Discount)
admin.site.register(Product)
admin.site.register(OrderDetail)
admin.site.register(PaymentDetail)
admin.site.register(UserPayment)
admin.site.register(UserAddress)
admin.site.register(OrderItems)
admin.site.register(CartItem)
admin.site.register(ShoppingSession)
