# Generated by Django 3.1.7 on 2021-04-23 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_auto_20210423_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_profile',
            name='profile_picture',
            field=models.ImageField(default='media/default/download.png', upload_to='pics'),
        ),
    ]
