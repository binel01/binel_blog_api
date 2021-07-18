from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers

from .models import CustomUser, Category, Post, Comment

class CustomUserSerializer(serializers.ModelSerializer):
    """
    Used to serialise/deserialize Users
    """
    class Meta:
        model = CustomUser
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):
    """
    Used to serialize/deserialize Categories
    """
    class Meta:
        model = Category
        fields = ['name', 'description', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    """
    Used to serialize/deserialize Posts
    """
    #category = CategorySerializer()
    #user = CustomUserSerializer()

    class Meta:
        model = Post
        fields = ['title', 'content', 'cover_image', 'category', 'user', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    """
    used to serialize/deserialize Comments
    """
    #post = PostSerializer()
    #user = CustomUserSerializer()

    class Meta:
        model = Comment
        fields = ['content', 'post', 'user', 'created_at']
