# Generated by Django 5.1.2 on 2024-10-25 16:34

import Booking.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ticket_id',
            field=models.CharField(default=Booking.models.generate_ticket_id, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
