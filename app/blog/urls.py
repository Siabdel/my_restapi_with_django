from django.contrib import admin
from django.urls import path, include
from . import views as b_views

urlpatterns = [
    path('<int:pk>/',  b_views.PostDetail.as_view(), ), # new
    path('',  b_views.PostList.as_view(), ), # new
]