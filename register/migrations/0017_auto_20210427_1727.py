# Generated by Django 3.1.7 on 2021-04-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_auto_20210427_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_profile',
            name='aadhar_id',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='new_profile',
            name='contact_no',
            field=models.BigIntegerField(default=0),
        ),
    ]
