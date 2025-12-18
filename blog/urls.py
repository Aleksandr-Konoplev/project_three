from blog.apps import BlogConfig
from django.urls import path
from blog.views import PostsListView


app_name = BlogConfig.name


urlpatterns = [
    path('posts_list', PostsListView.as_view(), name='posts_list'),
]