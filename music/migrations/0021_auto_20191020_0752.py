# Generated by Django 2.0.6 on 2019-10-20 07:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0020_auto_20191020_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='movielist',
            name='language',
            field=models.CharField(default='english', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movielist',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 7, 51, 48, 65184, tzinfo=utc)),
        ),
    ]
