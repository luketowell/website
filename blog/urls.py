from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="homepage"),
    path("posts", views.AllPostView.as_view(), name="posts"),
    path("posts/<slug>", views.single_post, name="post-detail-page")
]
