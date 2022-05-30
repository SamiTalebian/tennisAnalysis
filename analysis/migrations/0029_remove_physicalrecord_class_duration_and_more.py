# Generated by Django 4.0.4 on 2022-05-30 06:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0028_alter_technicalrecord_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='physicalrecord',
            name='class_duration',
        ),
        migrations.RemoveField(
            model_name='technicalrecord',
            name='class_duration',
        ),
        migrations.CreateModel(
            name='StaffRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', django_jalali.db.models.jDateField(auto_now_add=True)),
                ('class_duration', models.FloatField(default=1)),
                ('mark', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staffs_sr', to='analysis.staff')),
            ],
        ),
    ]
