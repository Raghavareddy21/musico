# Generated by Django 2.0.6 on 2019-04-04 15:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0016_auto_20180729_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 4, 15, 13, 34, 165845, tzinfo=utc)),
        ),
    ]
