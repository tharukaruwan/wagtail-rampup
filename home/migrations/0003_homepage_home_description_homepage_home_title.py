# Generated by Django 4.0.2 on 2022-02-10 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='home_description',
            field=models.CharField(default='Home Page Description', max_length=100),
        ),
        migrations.AddField(
            model_name='homepage',
            name='home_title',
            field=models.CharField(default='Home Page', max_length=100),
        ),
    ]
