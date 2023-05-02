from django.shortcuts import render
# Create your views here.

# postapi/views.py
from rest_framework import generics
from .models import BlogApi
from .serilizers import PostApiSerializer 


class PostList(generics.ListCreateAPIView):
    serializer_class = PostApiSerializer
    queryset = BlogApi.objects.all()
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogApi.objects.all()
    serilizer_class = PostApiSerializer
    
    
