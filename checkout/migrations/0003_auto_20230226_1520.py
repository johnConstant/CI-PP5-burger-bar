# Generated by Django 3.2.16 on 2023-02-26 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_auto_20230130_2127'),
        ('checkout', '0002_auto_20230225_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_type',
            field=models.CharField(choices=[('delivery', 'Delivery'), ('collection', 'Collection')], default=None, max_length=32),
        ),
        migrations.AlterField(
            model_name='orderlineitem',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_item', to='menu.menu_item'),
        ),
    ]
