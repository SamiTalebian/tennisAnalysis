# Generated by Django 4.0.4 on 2022-05-30 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0026_remove_technicalrecord_player_technicalrecord_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technicalrecord',
            name='player',
        ),
        migrations.AddField(
            model_name='technicalrecord',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='analysis.player'),
        ),
        migrations.AlterField(
            model_name='technicalrecord',
            name='staff',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='staffs', to='analysis.staff'),
        ),
    ]