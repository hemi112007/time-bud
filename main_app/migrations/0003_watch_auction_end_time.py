# Generated by Django 4.2.20 on 2025-05-05 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_watch_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='watch',
            name='auction_end_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 5, 12, 16, 31, 45, 867708, tzinfo=datetime.timezone.utc)),
        ),
    ]
