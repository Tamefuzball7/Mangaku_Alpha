# Generated by Django 4.2 on 2023-05-26 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangaku', '0012_alter_profile_fondo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='fondo',
            field=models.ImageField(default='', upload_to='profile_fondos'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='', upload_to='profile_pics'),
        ),
    ]
