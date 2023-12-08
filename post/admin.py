from django.contrib import admin
from post.models import Product, Category, Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'rate', 'created_at']
    list_editable = ['rate']
    list_filter = ['categories', 'created_at']
    search_fields = ['title', 'content']

admin.site.register(Category)
admin.site.register(Comment)
