from django.contrib import admin
from product.models import product, Category

admin.site.register(product)
admin.site.register(Category)