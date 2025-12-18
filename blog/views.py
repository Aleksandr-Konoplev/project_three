from django.urls import reverse_lazy

from blog.models import Post

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


class PostsListView(ListView):
    model = Post
    template_name = 'blog/posts_list.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    fields = ('title', 'content', 'image',)
    success_url = reverse_lazy(':pass')


class PostUpdateView(UpdateView):
    model = Post
    pass


class PostDeleteView(DeleteView):
    model = Post
    pass