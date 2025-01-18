from django.contrib import admin
from .models import Post, Author, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug": ("title",)}
    list_filter = ('title', 'author')
    list_display = ('title', 'author', 'date')

class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("first_name", "last_name")
    list_display = ("id", "first_name", "last_name")


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Tag)