# Generated by Django 2.0.6 on 2019-04-08 14:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0017_auto_20190404_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 8, 14, 29, 11, 307927, tzinfo=utc)),
        ),
    ]
