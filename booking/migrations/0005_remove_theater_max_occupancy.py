# Generated by Django 2.1.7 on 2019-04-14 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_theater_seating_chart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theater',
            name='max_occupancy',
        ),
    ]
