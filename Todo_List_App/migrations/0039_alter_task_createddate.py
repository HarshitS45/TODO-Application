# Generated by Django 4.2 on 2023-06-14 15:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo_List_App', '0038_alter_profile_profile_picture_alter_task_createddate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdDate',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 14, 15, 9, 14, 813456, tzinfo=datetime.timezone.utc)),
        ),
    ]