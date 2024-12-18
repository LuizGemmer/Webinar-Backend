# Generated by Django 5.1.1 on 2024-11-20 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_picture', models.ImageField(upload_to='uploads/profile_pictures')),
                ('about_me', models.TextField(blank=True)),
                ('serial_number', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='profile_picture',
        ),
    ]
