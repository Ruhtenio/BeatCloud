# Generated by Django 4.2.1 on 2023-06-07 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_webpaytransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='sus',
            field=models.ManyToManyField(to='app.suscripcion'),
        ),
    ]
