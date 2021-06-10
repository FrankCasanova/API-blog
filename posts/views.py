from rest_framework import generics
from .models import Post
from .serializers import PostSearializer


# Create your views here.


class PostList(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSearializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSearializer
