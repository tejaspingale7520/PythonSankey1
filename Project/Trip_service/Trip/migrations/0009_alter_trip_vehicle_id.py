# Generated by Django 5.1.2 on 2024-10-25 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trip', '0008_alter_trip_trip_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='vehicle_id',
            field=models.IntegerField(unique=True),
        ),
    ]
