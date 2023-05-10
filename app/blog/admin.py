from django.contrib import admin

# Register your models here.

from .models import BlogApi


class BlogApiAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'created_at',)
    
admin.site.register(BlogApi, BlogApiAdmin)
