# Generated by Django 3.2.13 on 2022-11-01 02:45

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(upload_to='avatars')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='avatars')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('themes', models.CharField(choices=[('힐링', '힐링'), ('액티비티', '액티비티')], max_length=4)),
            ],
        ),
    ]
