# Generated by Django 5.1.1 on 2024-10-30 00:57

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the sector. Must be unique.', max_length=255, unique=True)),
                ('description', models.TextField(help_text='Specify what part of the organization this sector represents.')),
            ],
        ),
        migrations.CreateModel(
            name='UserFunctionPermissions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('permission_type', models.CharField(choices=[('admin', 'admin'), ('supervisor', 'supervisor'), ('manager', 'manager'), ('viewer', 'viewer')], max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserPermissionTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_permission_type', models.CharField(choices=[('admin', 'admin'), ('supervisor', 'supervisor'), ('manager', 'manager'), ('viewer', 'viewer')], default='viewer', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserSectorPermissions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('permission_type', models.CharField(choices=[('admin', 'admin'), ('supervisor', 'supervisor'), ('manager', 'manager'), ('viewer', 'viewer')], max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSubsectorPermissions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('permission_type', models.CharField(choices=[('admin', 'admin'), ('supervisor', 'supervisor'), ('manager', 'manager'), ('viewer', 'viewer')], max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subsector',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the subsector.', max_length=255)),
                ('description', models.TextField(help_text='Specify what part of the sector this subsector represents.')),
                ('is_active', models.BooleanField(help_text='Soft delete boolean')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permissions.sector')),
            ],
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the function.', max_length=255)),
                ('description', models.TextField(help_text='Specify what the function is all about.')),
                ('is_active', models.BooleanField(help_text='Soft delete boolean')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Subsector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='permissions.subsector')),
            ],
        ),
    ]
