# Generated by Django 4.2 on 2023-05-25 20:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mangaku', '0008_comment_dislikes_comment_comment_likes_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislikes_comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='likes_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='disliked_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
