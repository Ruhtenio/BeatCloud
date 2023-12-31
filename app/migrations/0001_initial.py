# Generated by Django 4.2.1 on 2023-05-29 02:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genero_Musical',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(choices=[(1, 'Pop'), (2, 'Rock'), (3, 'Hip-Hop'), (4, 'Electronica'), (5, 'Reggaeton'), (6, 'R&B'), (7, 'Jazz'), (8, 'Metal'), (9, 'Soul')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id_track', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_track', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('track', models.FileField(upload_to='canciones')),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('foto', models.ImageField(null=True, upload_to='tracks')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.genero_musical')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('tipo_usu', models.IntegerField(choices=[(1, 'Artista'), (2, 'Productor')])),
                ('foto_perfil', models.ImageField(blank=True, null=True, upload_to='media/perfil')),
                ('foto_fondo', models.ImageField(blank=True, null=True, upload_to='media/fondo')),
                ('spotify', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('carrito1', models.ManyToManyField(related_name='usuarios_en_carrito', to='app.track')),
                ('tracks_gustados', models.ManyToManyField(related_name='usuarios_que_dieron_like', to='app.track')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('precio', models.IntegerField()),
                ('iva', models.IntegerField()),
                ('precio_total', models.IntegerField()),
                ('completada', models.BooleanField(default=False)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.track')),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='track',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario'),
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id_sus', models.AutoField(primary_key=True, serialize=False)),
                ('detalle', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Metodo_Pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=200)),
                ('venta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.venta')),
            ],
        ),
        migrations.CreateModel(
            name='Interes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.genero_musical')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateTimeField(auto_now_add=True)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.track')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.venta')),
            ],
            options={
                'verbose_name_plural': 'Historial de compras',
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='app.track')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('precio', models.IntegerField()),
                ('iva', models.IntegerField()),
                ('precio_total', models.IntegerField()),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.track')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario')),
            ],
        ),
    ]
