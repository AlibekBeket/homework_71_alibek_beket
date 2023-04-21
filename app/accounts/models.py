from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices

from accounts.managers import UserManager


# Create your models here.

class ProfileGenderChoice(TextChoices):
    MALE = 'male', 'Мужчина'
    FEMALE = 'female', 'Женщина'


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='Адрес электронные почты',
        unique=True,
        blank=False
    )
    avatar = models.ImageField(
        null=False,
        blank=False,
        upload_to='user_img',
        verbose_name='Аватарка'
    )
    user_description = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        verbose_name="Информация о пользователе"
    )
    phone_number = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        verbose_name='Номер телефона',
    )
    gender = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Пол',
        choices=ProfileGenderChoice.choices
    )
    number_of_publications = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Количество публикаций",
        default=0
    )
    number_of_subscriptions = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Количество подписок",
        default=0
    )
    number_of_subscribers = models.IntegerField(
        null=False,
        blank=False,
        verbose_name="Количество подписчиков",
        default=0
    )
    liked_posts = models.ManyToManyField(
        to='instagram.Posts',
        blank=True,
        verbose_name='Понравившиеся публикации',
        related_name='user_likes'
    )
    subscriptions = models.ManyToManyField(
        to='accounts.Account',
        blank=True,
        verbose_name='Подписки',
        related_name='subscription'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    object = UserManager()

    class Meta:
        verbose_name = 'Профиль',
        verbose_name_plural = 'Профиль'
