# Generated by Django 4.0.2 on 2022-02-10 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerOrder',
            fields=[
                ('orderId', models.AutoField(primary_key=True, serialize=False)),
                ('orderCreatedDate', models.DateField()),
                ('itemCount', models.IntegerField(blank=True)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('customer', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, related_name='order', to='customer.customer')),
            ],
        ),
    ]
