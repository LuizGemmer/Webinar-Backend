# Generated by Django 5.1.1 on 2024-09-25 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='function',
        ),
        migrations.RemoveField(
            model_name='subsector',
            name='sector',
        ),
        migrations.DeleteModel(
            name='Function',
        ),
        migrations.DeleteModel(
            name='Sector',
        ),
        migrations.DeleteModel(
            name='Subsector',
        ),
    ]