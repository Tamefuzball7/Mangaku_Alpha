# Generated by Django 4.2 on 2023-05-26 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangaku', '0011_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fondo',
            field=models.ImageField(default='default.jpg', upload_to='profile_fondos'),
        ),
    ]
