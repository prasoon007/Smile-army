# Generated by Django 3.1.7 on 2021-04-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0013_auto_20210425_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_profile',
            name='profile_picture',
            field=models.ImageField(default='media/default/download.jpg', upload_to='pics'),
        ),
    ]