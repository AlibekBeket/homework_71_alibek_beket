# Generated by Django 4.1.7 on 2023-03-28 04:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_remove_comments_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания комментария'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='posts',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата публикации поста'),
            preserve_default=False,
        ),
    ]
