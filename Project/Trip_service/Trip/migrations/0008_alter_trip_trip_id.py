# Generated by Django 5.1.2 on 2024-10-25 16:11

import Trip.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0007_alter_trip_trip_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_id',
            field=models.CharField(default=Trip.models.generate_trip_id, editable=False, max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]