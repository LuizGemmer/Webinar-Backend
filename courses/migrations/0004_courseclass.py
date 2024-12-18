# Generated by Django 5.1.1 on 2024-11-05 23:37

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_usercoursehistory_date_submited_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseClass',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Title/Name of the class', max_length=255)),
                ('description', models.TextField(help_text='A description of the class. use it to signal what it teaches, how the user should aprouch it and whatever else you like')),
                ('class_file', models.FileField(help_text='The path to the file', upload_to='courses/classes/')),
                ('sequence_in_course', models.IntegerField(help_text='Sets which sequence the classes in the course must be shown. Starts from 1', validators=[django.core.validators.MinValueValidator(1)])),
                ('class_file_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video'), ('pdf', 'PDF')], help_text='Saves the type of file to be stored', max_length=5)),
                ('is_active', models.BooleanField(help_text='Soft delete boolean')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.course')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_classes', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='last_modified_classes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
