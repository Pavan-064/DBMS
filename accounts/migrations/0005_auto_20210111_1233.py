# Generated by Django 3.1.3 on 2021-01-11 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210103_1203'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='paid_amount',
            new_name='due_amount',
        ),
    ]