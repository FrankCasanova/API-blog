from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework import viewsets
from .models import Post
from .serializers import PostSearializer, UserSerializer
from .persmissions import IsAuthorOrReadOnly


# Create your views here.


# class PostList(generics.ListCreateAPIView):

#     queryset = Post.objects.all()
#     serializer_class = PostSearializer


# class PostDetail(generics.RetrieveUpdateDestroyAPIView):

#     permission_classes = (IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSearializer

class PostViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSearializer


# class UserList(generics.ListCreateAPIView):

#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveDestroyAPIView):

#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
