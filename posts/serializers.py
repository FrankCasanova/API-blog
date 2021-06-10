from rest_framework import serializers
from rest_framework.utils import field_mapping, model_meta
from .models import Post


class PostSearializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at')
