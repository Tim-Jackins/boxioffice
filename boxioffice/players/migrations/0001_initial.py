# Generated by Django 2.1.7 on 2019-03-18 23:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('bio', models.TextField(max_length=280)),
                ('headshot', models.ImageField(help_text='Make sure your headshot is 8in x 10in.', upload_to='headshots')),
                ('user_logged_in', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ensemble', models.BooleanField(default=True)),
                ('part_name', models.CharField(default='', max_length=15)),
                ('main_actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_actor', related_query_name='main_actor', to='players.Actor')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.Show')),
                ('understudy1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='understudy1_actor', related_query_name='understudy1_actor', to='players.Actor')),
                ('understudy2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='understudy2_actor', related_query_name='understudy2_actor', to='players.Actor')),
            ],
        ),
    ]
