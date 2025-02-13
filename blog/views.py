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

    def isStoredPost(self, request, post_id):
        stored_posts = request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False

        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.isStoredPost(request, post.id)
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
        print(f'errors: {comment_form.errors}')
        context = {
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.isStoredPost(request, post.id)
        }
        return render(request, "blog/post-detail.html", context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context={
                
            }
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else: 
            posts = Post.objects.filter(id__in = stored_posts)

            context["posts"] = posts
            context["has_posts"]=True
            print(f"posts: {context["posts"]}")
            
        
        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        post_id = request.POST["post_id"]
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []
            
        if int(post_id) not in stored_posts:
            stored_posts.append(int(request.POST["post_id"]))
            request.session["stored_posts"] = stored_posts
        else: 
            print(f"stored post pre-removal: {stored_posts}")
            stored_posts.remove(int(post_id))
            request.session["stored_posts"] = stored_posts

        print(f"stored post post-removal: {stored_posts}")
        return HttpResponseRedirect("/")