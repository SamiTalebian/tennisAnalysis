# Generated by Django 4.0.4 on 2022-05-20 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0019_remove_staff_payment_payment_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment',
            new_name='staff',
        ),
    ]
