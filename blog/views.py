from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "blog/index.html")

def all_posts(request):
    return render(request, "blog/all-posts.html")

def single_post(request):
    pass