# Generated by Django 3.2.8 on 2021-11-03 12:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20211103_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 12, 30, 39, 202877, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='address',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 12, 30, 39, 202890, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 12, 30, 39, 201815, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 12, 30, 39, 201828, tzinfo=utc)),
        ),
    ]
