# Generated by Django 2.0.6 on 2018-07-19 06:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_auto_20180712_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 19, 6, 35, 47, 815505, tzinfo=utc)),
        ),
    ]
