from rest_framework import response
from blog_api.serializers import PostSerializer
from .serializers import UserSerializer 
from blog_api.models import Post
from rest_framework import generics, serializers
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework import status
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

#All post view/Home View

class PostList(generics.ListAPIView):
    permission_classes=[IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().order_by('-id')
    serializer_class = PostSerializer

#User Login And Registration

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes =[AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

#User post view

class UserPostList(generics.ListAPIView):
    permission_classes =[IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author = user).order_by('-id')

#User Actions
#User Create Post

class PostCreate(generics.CreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset=Post.objects.all
    serializer_class =PostSerializer

#User Get,Update,Delete Post

class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class = PostSerializer
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)

