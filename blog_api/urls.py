from django.contrib import admin
from django.urls import path
from django.views.generic.base import View
from  users.views import PostDetails, PostList, PostCreate, UserPostList
from users.views import RegisterAPI
from knox import views as knox_views
from users.views import LoginAPI

app_name='blog_api'

urlpatterns = [
    path('',PostList.as_view(),name='post_view'),
    #User
    path('user/posts/',UserPostList.as_view(),name='user_post_list'),
    path('user/create/',PostCreate.as_view(),name='post_create'),
    path('user/post/detail/<int:pk>',PostDetails.as_view(),name='post_details'),
    #Register and Login
    path('user/register/', RegisterAPI.as_view(), name='register'),
    path('user/login/', LoginAPI.as_view(), name='login'),
    path('user/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('user/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    
]