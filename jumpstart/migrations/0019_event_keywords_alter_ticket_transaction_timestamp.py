# Generated by Django 4.1.7 on 2023-03-26 13:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumpstart', '0018_alter_ticket_transaction_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='keywords',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='transaction_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 13, 34, 50, 55048, tzinfo=datetime.timezone.utc)),
        ),
    ]
