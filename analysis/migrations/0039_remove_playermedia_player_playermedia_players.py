# Generated by Django 4.0.4 on 2022-07-25 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0038_alter_playermedia_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playermedia',
            name='player',
        ),
        migrations.AddField(
            model_name='playermedia',
            name='players',
            field=models.ManyToManyField(related_name='player_media', to='analysis.player'),
        ),
    ]
