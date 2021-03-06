# Generated by Django 3.1.7 on 2021-04-16 06:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='aadhar_id',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pin',
            field=models.IntegerField(max_length=8),
        ),
        migrations.CreateModel(
            name='new_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.BigIntegerField()),
                ('upload_on', models.DateTimeField(auto_now_add=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='pics')),
                ('address', models.TextField()),
                ('pin', models.IntegerField(max_length=8)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('aadhar_id', models.BigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
