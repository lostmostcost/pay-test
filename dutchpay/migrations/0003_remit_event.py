# Generated by Django 5.0 on 2024-01-03 05:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dutchpay', '0002_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='remit',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='remits', to='dutchpay.event'),
        ),
    ]