# Generated by Django 4.2 on 2023-04-11 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='feed',
            new_name='all_feed',
        ),
    ]
