# Generated by Django 4.0 on 2021-12-21 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OtderItem',
            new_name='OrderItem',
        ),
    ]
