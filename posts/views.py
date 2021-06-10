from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSearializer
from .persmissions import IsAuthorOrReadOnly


# Create your views here.


class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSearializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSearializer
