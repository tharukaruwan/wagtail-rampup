# Generated by Django 4.0.2 on 2022-02-23 11:59

import django.contrib.auth.models
from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_managers_alter_account_is_admin_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='account',
            managers=[
                ('object', django.db.models.manager.Manager()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
