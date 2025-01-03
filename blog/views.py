from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "blog/index.html")

def all_posts(request):
    pass

def single_post(request):
    pass