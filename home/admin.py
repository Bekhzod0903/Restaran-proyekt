# admin.py
from django.contrib import admin
from .models import Food,Category,CartItem

admin.site.register(Food)
admin.site.register(Category)
admin.site.register(CartItem)