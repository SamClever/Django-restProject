# Generated by Django 5.1.7 on 2025-03-28 11:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0002_streamplatform_watchlist_delete_movie'),
    ]

    operations = [
        migrations.RenameField(
            model_name='watchlist',
            old_name='create',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='watchlist',
            old_name='stortline',
            new_name='storyline',
        ),
    ]
