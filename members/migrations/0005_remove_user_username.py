# Generated by Django 5.0 on 2023-12-30 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
