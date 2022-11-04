# Generated by Django 3.2.13 on 2022-11-04 04:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[(None, '선택'), ('서울', '서울'), ('제주', '제주'), ('부산', '부산')], default='선택', max_length=2)),
                ('content', models.TextField()),
                ('title', models.CharField(max_length=80)),
                ('subtitle', models.CharField(max_length=80)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='media/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('start_day', models.DateField(default=datetime.date.today, help_text='날짜 및 시간')),
                ('end_day', models.DateField(default=datetime.date.today, help_text='날짜 및 시간')),
                ('hits', models.PositiveIntegerField(default=0)),
                ('like', models.ManyToManyField(blank=True, related_name='review_like', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
