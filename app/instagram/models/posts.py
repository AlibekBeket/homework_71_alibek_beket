from django.contrib.auth import get_user_model
from django.db import models


class Posts(models.Model):
    user = models.ForeignKey(
        to=get_user_model(),
        related_name='user_post',
        null=False,
        blank=False,
        verbose_name='Автор',
        on_delete=models.CASCADE
    )
    description = models.TextField(
        max_length=1000,
        null=False,
        blank=False,
        verbose_name="Текст поста"
    )
    img = models.ImageField(
        null=False,
        blank=False,
        upload_to='post_img',
        verbose_name='Фото'
    )
    likes = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Количество лайков в посте",
        default=0
    )
    comments = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Количество комментариев в посте",
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации поста'
    )

    def __str__(self):
        return f'{self.user} - {self.likes}'
