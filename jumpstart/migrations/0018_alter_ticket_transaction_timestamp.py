# Generated by Django 4.1.7 on 2023-03-26 04:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jumpstart', '0017_remove_ticket_spl_adult_tickets_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='transaction_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 26, 4, 21, 28, 503871, tzinfo=datetime.timezone.utc)),
        ),
    ]