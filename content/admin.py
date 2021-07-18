from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'cover_image', 'category', 'user', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'user', 'created_at')

