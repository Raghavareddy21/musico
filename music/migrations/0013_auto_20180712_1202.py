# Generated by Django 2.0.6 on 2018-07-12 12:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0012_auto_20180711_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 12, 12, 2, 5, 195939, tzinfo=utc)),
        ),
    ]