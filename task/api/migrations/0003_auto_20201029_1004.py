# Generated by Django 3.1.2 on 2020-10-29 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201029_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmanagement',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='taskmanagement',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]