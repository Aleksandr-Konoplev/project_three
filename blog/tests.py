from django.test import TestCase
from django.urls import reverse

from blog.models import Post


class PostModelTests(TestCase):
    def test_str_truncates_long_content(self):
        post = Post.objects.create(
            title="Тестовый пост",
            content="12345678901234567890123456789012345",
        )

        self.assertEqual(str(post), "Тестовый пост 123456789012345678901234567890...")


class PostViewTests(TestCase):
    def test_post_detail_increments_views_count(self):
        post = Post.objects.create(
            title="Тестовый пост",
            content="Короткий текст",
            publication_flag=True,
        )

        response = self.client.get(reverse("blog:post_detail", args=[post.pk]))

        post.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(post.views_count, 1)
