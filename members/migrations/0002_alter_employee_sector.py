# Generated by Django 5.0 on 2023-12-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='sector',
            field=models.ManyToManyField(null=True, to='members.sector'),
        ),
    ]
