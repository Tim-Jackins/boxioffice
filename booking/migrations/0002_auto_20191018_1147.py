# Generated by Django 2.2.6 on 2019-10-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='SeatNumber',
            field=models.IntegerField(default=1),
        ),
    ]
