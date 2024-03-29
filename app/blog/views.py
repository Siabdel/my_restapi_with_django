from django.shortcuts import render
# Create your views here.


# postapi/views.py
from rest_framework import generics, permissions
from .models import BlogApi
from .serializers import PostApiSerializer 
from .permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    serializer_class = PostApiSerializer
    queryset = BlogApi.objects.all().order_by('-created_at')
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthorOrReadOnly, )
    serializer_class = PostApiSerializer
    queryset = BlogApi.objects.all()
    
    
