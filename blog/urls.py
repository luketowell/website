from django.urls import path

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug>", views.single_post, name="post-detail-page")
]
