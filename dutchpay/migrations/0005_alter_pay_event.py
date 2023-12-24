# Generated by Django 5.0 on 2023-12-24 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dutchpay', '0004_alter_pay_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pay',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='dutchpay.event'),
        ),
    ]