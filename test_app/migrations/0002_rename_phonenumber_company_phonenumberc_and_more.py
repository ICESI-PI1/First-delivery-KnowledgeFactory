# Generated by Django 4.2.1 on 2023-05-09 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='phoneNumber',
            new_name='phoneNumberC',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='phoneNumber',
            new_name='phoneNumberU',
        ),
    ]
