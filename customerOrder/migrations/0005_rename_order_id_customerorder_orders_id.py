# Generated by Django 4.0.2 on 2022-02-14 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerOrder', '0004_alter_customerorder_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerorder',
            old_name='order_id',
            new_name='orders_id',
        ),
    ]
