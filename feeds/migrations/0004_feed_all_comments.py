# Generated by Django 4.2 on 2023-04-11 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_rename_feed_comment_all_feed'),
        ('feeds', '0003_feed_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='all_comments',
            field=models.ManyToManyField(blank=True, to='comments.comment'),
        ),
    ]
