from django.urls import reverse_lazy

from blog.models import Post

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView


class PostsListView(ListView):
    model = Post
    template_name = "blog/posts_list.html"
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(publication_flag=True)
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = (
        "title",
        "content",
        "image",
        "publication_flag",
    )
    success_url = reverse_lazy("blog:posts_list")


class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = (
        "title",
        "content",
        "image",
    )

    def get_success_url(self):
        return reverse_lazy("blog:post_detail", kwargs={"pk": self.object.pk})


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy("blog:posts_list")
