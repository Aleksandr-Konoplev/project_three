from blog.apps import BlogConfig
from django.urls import path
from blog.views import (
    PostsListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)


app_name = BlogConfig.name

urlpatterns = [
    path("posts/", PostsListView.as_view(), name="posts_list"),
    path("posts/create/", PostCreateView.as_view(), name="post_create"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
]
