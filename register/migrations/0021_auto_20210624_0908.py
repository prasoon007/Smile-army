# Generated by Django 3.1.7 on 2021-06-24 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0020_auto_20210624_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_profile',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
