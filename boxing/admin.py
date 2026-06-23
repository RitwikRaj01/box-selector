from django.contrib import admin
from .models import Box, Product, Order, OrderItem

admin.site.register(Box)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)