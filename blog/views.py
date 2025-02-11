from datetime import date
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Post
from .forms import CommentForm


class HomePageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    
class AllPostView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

class SinglePostView(View):

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        post_tags = post.tags.all()
        comment_form = CommentForm()
        context = {
            "post": post,
            "post_tags": post_tags,
            "comment_form": comment_form
        }
        return render(request, "blog/post-detail.html", context)


    def post(self, request, slug):
        comment_form = CommentForm(request.POST)

        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail-page', args=[slug] ))
        
        
        post_tags = post.tags.all()
        comment_form = CommentForm()
        context = {
            "post": post,
            "post_tags": post_tags,
            "comment_form": comment_form
        }
        return render(request, "blog/post-detail.html", context)

