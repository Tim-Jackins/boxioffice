# Generated by Django 2.2.6 on 2019-10-18 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_show_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='AreaDesc',
            field=models.CharField(default='standard', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='PhyRowId',
            field=models.CharField(default='X', max_length=50),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='seatId',
            field=models.CharField(default='X1', max_length=50),
        ),
    ]
