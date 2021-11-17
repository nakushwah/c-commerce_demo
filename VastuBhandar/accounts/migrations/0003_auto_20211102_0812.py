# Generated by Django 3.2.8 on 2021-11-02 08:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211102_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 8, 12, 26, 831943, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='address',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 8, 12, 26, 831959, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 8, 12, 26, 830413, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 8, 12, 26, 830438, tzinfo=utc)),
        ),
    ]