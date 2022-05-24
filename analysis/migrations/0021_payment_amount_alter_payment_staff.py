# Generated by Django 4.0.4 on 2022-05-20 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0020_rename_payment_payment_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='payment',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payments', to='analysis.staff'),
        ),
    ]
