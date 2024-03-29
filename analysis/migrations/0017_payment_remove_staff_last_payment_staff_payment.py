# Generated by Django 4.0.4 on 2022-05-19 16:44

from django.db import migrations, models
import django.db.models.deletion
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0016_staff_last_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', django_jalali.db.models.jDateField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='staff',
            name='last_payment',
        ),
        migrations.AddField(
            model_name='staff',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='analysis.payment'),
        ),
    ]
