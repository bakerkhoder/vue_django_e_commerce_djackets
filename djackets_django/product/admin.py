from django.contrib import admin
from .models import Category, Product, Customer, Profile

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Profile)

# Register your models here.
