# Generated by Django 4.0.2 on 2022-02-10 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customerOrder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerorder',
            old_name='itemCount',
            new_name='item_count',
        ),
        migrations.RenameField(
            model_name='customerorder',
            old_name='orderCreatedDate',
            new_name='order_created_date',
        ),
        migrations.RenameField(
            model_name='customerorder',
            old_name='orderId',
            new_name='order_id',
        ),
    ]
