from datetime import date
from django.shortcuts import render

from .models import Post





# sort function
def get_date(post):
    return post['date']


# Create your views here.
def homepage(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, "blog/index.html", {
        "posts":latest_posts
        })

def posts(request):
    all_posts = Post.objects.all()
    return render(request, "blog/all-posts.html", {"posts": all_posts})

def single_post(request, slug):


    identified_post = Post.objects.get(slug = slug)

    return render(request, "blog/post-detail.html", {
        "post": identified_post
    } )