# Generated by Django 2.0.6 on 2018-06-20 09:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_auto_20180619_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 20, 9, 19, 15, 415259, tzinfo=utc)),
        ),
    ]
