# Generated by Django 2.0.6 on 2018-07-21 16:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0014_auto_20180719_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 21, 16, 25, 55, 673448, tzinfo=utc)),
        ),
    ]
