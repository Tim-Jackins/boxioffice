# Generated by Django 2.1.7 on 2019-04-14 15:10

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20190324_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='theater',
            name='seating_chart',
            field=jsonfield.fields.JSONField(default='', help_text='Enter the JSON seating chart'),
        ),
    ]