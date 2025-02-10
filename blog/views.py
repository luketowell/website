from datetime import date
from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


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
        
# sort function
def get_date(post):
    return post['date']

def single_post(request, slug):


    identified_post = Post.objects.get(slug = slug)

    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all() 
    } )