# Generated by Django 3.2.6 on 2021-08-26 06:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_app', '0002_item_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 26, 6, 23, 45, 3169, tzinfo=utc)),
        ),
    ]
