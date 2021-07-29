from typing import OrderedDict
from rest_framework import serializers
from django.db.models import fields
from blog_api.models import Post
from django.conf import settings

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','title','content','author')
        extra_kwargs = {
            "title": {"required":True},
            "content": {"required":True},
            "author": {"required":True},
        }