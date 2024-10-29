# Generated by Django 5.1.1 on 2024-09-26 13:43

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPermissionTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_permission_type', models.CharField(choices=[('admin', 'admin'), ('supervisor', 'supervisor'), ('manager', 'manager'), ('viewer', 'viewer')], default='viewer', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserFunctionPermissions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('permission_type', models.CharField(choices=[('admin', 'admin'), ('supervisor', 'supervisor'), ('manager', 'manager'), ('viewer', 'viewer')], max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='function_permissions_set', to=settings.AUTH_USER_MODEL)),
                ('function', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permissions.function')),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='function_permissions_modified', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSectorPermissions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('permission_type', models.CharField(choices=[('admin', 'admin'), ('supervisor', 'supervisor'), ('manager', 'manager'), ('viewer', 'viewer')], max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('Subsector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permissions.sector')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_permissions_set', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sector_permissions_modified', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSubsectorPermissions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('permission_type', models.CharField(choices=[('admin', 'admin'), ('supervisor', 'supervisor'), ('manager', 'manager'), ('viewer', 'viewer')], max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
                ('Subsector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permissions.subsector')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsector_permissions_set', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsector_permissions_modified', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]