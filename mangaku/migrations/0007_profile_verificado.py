# Generated by Django 4.2 on 2023-05-25 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangaku', '0006_alter_post_content_alter_post_imagen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='verificado',
            field=models.BooleanField(default=False),
        ),
    ]