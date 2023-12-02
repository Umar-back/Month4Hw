from django.contrib import admin

from post.models import Product, Hashtag, Comment

@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'rate', 'created_at']
    list_editable = ['rate']
    list_filter = ['hashtag', 'created_at']
    search_fields = ['title', 'content', 'hashtags_title']




admin.site.register(Hashtag)
admin.site.register(Comment)