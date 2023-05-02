# postapi/views.py
from rest_framework import serializers
from .models import BlogApi

class PostApiSerializer(serializers.ModelSerializer):
    class Meta :
        fields = ('id', 'title', 'body', 'created_at', )
        model = BlogApi
    