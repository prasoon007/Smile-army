# Generated by Django 3.1.7 on 2021-05-15 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210515_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cover_pic',
            field=models.FileField(upload_to='cat_pics'),
        ),
    ]
