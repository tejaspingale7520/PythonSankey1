# Generated by Django 5.1.2 on 2024-10-19 11:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Route', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('trip_id', models.CharField(default='TP00000000', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('user_id', models.IntegerField()),
                ('vehicle_id', models.IntegerField()),
                ('driver_name', models.CharField(max_length=255)),
                ('Route_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='Route.route')),
            ],
        ),
    ]
