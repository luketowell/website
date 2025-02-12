from django.contrib import admin
from .models import Post, Author, Tag, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}
    list_filter = ('title', 'author', 'tags')
    list_display = ('title', 'author', 'date')

class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("first_name", "last_name")
    list_display = ("id", "first_name", "last_name")

class CommentAdmin(admin.ModelAdmin):
    list_filter = ("user_name", "user_email", "post")
    list_display = ("id", "user_name", "user_email", "text", "post")

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)