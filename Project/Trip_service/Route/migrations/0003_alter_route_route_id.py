# Generated by Django 5.1.2 on 2024-10-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Route', '0002_alter_route_route_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='Route_id',
            field=models.CharField(default='RT82049765', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
