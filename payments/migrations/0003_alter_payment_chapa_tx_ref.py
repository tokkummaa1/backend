# Generated by Django 5.1.6 on 2025-02-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_chapa_tx_ref_payment_gateway'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='chapa_tx_ref',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
