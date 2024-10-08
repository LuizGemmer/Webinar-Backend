# Generated by Django 5.1.1 on 2024-09-26 18:52

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_course_function_remove_subsector_sector_and_more'),
        ('permissions', '0003_rename_subsector_usersectorpermissions_sector_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseFunction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('function', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_history', to='permissions.function')),
            ],
        ),
        migrations.CreateModel(
            name='UserCourseHistory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_history', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
