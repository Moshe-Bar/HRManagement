# Generated by Django 5.0 on 2023-12-25 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_companyadmin_employee_shiftmanager'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='productivity_rate',
            field=models.SmallIntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='members.company'),
        ),
    ]
