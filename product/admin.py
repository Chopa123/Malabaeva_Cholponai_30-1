from django.contrib import admin
from product.models import product, Category, Review

admin.site.register(product)
admin.site.register(Category)
admin.site.register(Review)
