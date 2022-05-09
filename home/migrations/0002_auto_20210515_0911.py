# Generated by Django 3.1.7 on 2021-05-15 03:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=250)),
                ('cover_pic', models.FileField(upload_to='')),
                ('description', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='services',
            name='feeder',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='services',
            name='cate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category'),
        ),
    ]
