# Generated by Django 2.0.6 on 2018-06-19 09:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20180613_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 6, 19, 9, 57, 23, 59897, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_location',
            field=models.FileField(upload_to=''),
        ),
    ]