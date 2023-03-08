# Generated by Django 3.2.16 on 2023-03-07 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20230130_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_item',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='menu_item',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
