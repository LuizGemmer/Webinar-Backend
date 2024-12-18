# Generated by Django 5.1.1 on 2024-11-17 20:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0004_rename_subsector_function_subsector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='function',
            name='subsector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funtions', to='permissions.subsector'),
        ),
        migrations.AlterField(
            model_name='userfunctionpermissions',
            name='function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_functions', to='permissions.function'),
        ),
    ]
