# Generated by Django 4.2.1 on 2023-05-30 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historialcompra',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.usuario'),
        ),
        migrations.AlterField(
            model_name='historialcompra',
            name='venta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.venta'),
        ),
    ]
