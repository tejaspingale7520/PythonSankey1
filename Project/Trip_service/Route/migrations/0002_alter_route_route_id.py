# Generated by Django 5.1.2 on 2024-10-24 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Route', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='Route_id',
            field=models.CharField(default='RT473922', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]
