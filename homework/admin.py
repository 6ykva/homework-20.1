from django.contrib import admin

from homework.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'category_id',)
    list_filter = ('category_id',)
    search_fields = ('name', 'descriptions',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
