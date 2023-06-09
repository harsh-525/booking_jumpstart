# Generated by Django 4.1.7 on 2023-03-25 04:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jumpstart', '0015_alter_ticket_transaction_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user_ptr',
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='customer', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='transaction_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 25, 4, 43, 7, 552159, tzinfo=datetime.timezone.utc)),
        ),
    ]
