# Generated by Django 3.2.16 on 2023-02-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='opening_hours',
        ),
        migrations.AddField(
            model_name='location',
            name='opening_hours',
            field=models.ManyToManyField(blank=True, related_name='opening_hours', to='location.Hours'),
        ),
    ]
