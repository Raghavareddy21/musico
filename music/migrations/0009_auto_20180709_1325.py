# Generated by Django 2.0.6 on 2018-07-09 13:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20180707_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 9, 13, 25, 24, 88816, tzinfo=utc)),
        ),
    ]