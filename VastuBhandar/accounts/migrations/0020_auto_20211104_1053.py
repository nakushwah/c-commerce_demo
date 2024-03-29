# Generated by Django 3.2.8 on 2021-11-04 10:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20211104_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 10, 53, 15, 498155, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='address',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 10, 53, 15, 498168, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 10, 53, 15, 497106, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 10, 53, 15, 497122, tzinfo=utc)),
        ),
    ]
