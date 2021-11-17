# Generated by Django 3.2.8 on 2021-11-03 12:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20211103_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 12, 13, 47, 949925, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='address',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 12, 13, 47, 949937, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 12, 13, 47, 948843, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 12, 13, 47, 948858, tzinfo=utc)),
        ),
    ]
