# Generated by Django 5.1.1 on 2024-10-30 00:57

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Title/Name of the course', max_length=255)),
                ('description', models.TextField(help_text='A description of the course. use it to signal what it teaches, how the user should aprouch it and whatever else you like')),
                ('expiration_time_in_days', models.IntegerField(default=365, help_text='\n        How long it will take for the course certification to expire in days.\n        If you want for it to not expire, set to a big number like: 99999\n        ')),
                ('required_for_function', models.BooleanField(default=True, help_text='\n        Defines if the course is needed for the function status to be set to "apt".\n        If true, the user can only be "apt" if this course is completed.\n        If false, this will be a complementary course, allowing the user to be "apt" even if not he has not compleated the course \n        ')),
                ('is_active', models.BooleanField(help_text='Soft delete boolean')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseFunction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserCourseHistory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]
