# Generated by Django 4.2 on 2023-05-25 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangaku', '0004_alter_comment_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='imagen',
            field=models.ImageField(default='', upload_to='image_posts'),
        ),
    ]