from django.db import models
from django.db.models.manager import Manager


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок поста', help_text='Введите заголовок')
    content = models.TextField(verbose_name='Текст поста', help_text='Введите текст')
    image = models.ImageField(upload_to='img_of_blog_post/', blank=True, null=True, verbose_name='Изображение для поста блога')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания поста')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования поста')
    publication_flag = models.BooleanField(default=False, verbose_name='Признак публикации')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    # Для линтера
    objects: Manager['Post']

    def __str__(self):
        result_content = str(self.content)
        if len(result_content) > 30:
            result_content = result_content[:30] + '...'
        return f'{self.title} {result_content}'

    def __repr__(self):
        result_content = str(self.content)
        if len(result_content) > 30:
            result_content = result_content[:30] + '...'
        return f'{self.title} {result_content}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['created_at']
