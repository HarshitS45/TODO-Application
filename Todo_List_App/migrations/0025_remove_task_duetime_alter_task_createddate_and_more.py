# Generated by Django 4.2 on 2023-06-12 14:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0024_task_duetime_alter_task_createddate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='dueTime',
        ),
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 12, 14, 9, 51, 922255, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='dueDate',
            field=models.DateTimeField(),
        ),
    ]
