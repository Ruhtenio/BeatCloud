# Generated by Django 4.2.1 on 2023-05-30 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_compra_venta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historialcompra',
            name='venta',
        ),
    ]