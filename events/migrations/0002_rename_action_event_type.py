# Generated by Django 4.2.1 on 2023-06-03 01:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='action',
            new_name='type',
        ),
    ]
