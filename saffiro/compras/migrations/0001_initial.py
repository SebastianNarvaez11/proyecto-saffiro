# Generated by Django 2.2.3 on 2020-02-16 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0003_auto_20200209_2228'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventario', '0008_auto_20200216_1012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('edicion', models.DateTimeField(auto_now=True)),
                ('codigo', models.IntegerField(verbose_name='Codigo')),
                ('observacion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Observacion')),
                ('sub_total', models.FloatField(default=0, verbose_name='Sub Total')),
                ('descuento', models.FloatField(default=0, verbose_name='Descuento')),
                ('total', models.FloatField(default=0, verbose_name='Total')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Empresa', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Compra',
                'verbose_name_plural': 'Compras',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('edicion', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('direccion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Direccion')),
                ('contacto', models.CharField(max_length=100, verbose_name='Contacto')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
                ('email', models.CharField(blank=True, max_length=250, null=True, verbose_name='Email')),
                ('user_create', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_update', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='DetalleCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('creacion', models.DateTimeField(auto_now_add=True)),
                ('edicion', models.DateTimeField(auto_now=True)),
                ('cantidad', models.BigIntegerField(default=0, verbose_name='Cantidad')),
                ('precio_compra', models.FloatField(default=0, verbose_name='Precio de compra')),
                ('sub_total', models.FloatField(default=0, verbose_name='Sub-Total')),
                ('descuento', models.FloatField(blank=True, default=0, null=True, verbose_name='Descuento')),
                ('total', models.FloatField(default=0, verbose_name='Total')),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Compra', verbose_name='Compra')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Producto', verbose_name='Producto')),
                ('user_create', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user_update', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detalle Compra',
                'verbose_name_plural': 'Detalles Compra',
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Proveedor', verbose_name='Proveedor'),
        ),
        migrations.AddField(
            model_name='compra',
            name='user_create',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='compra',
            name='user_update',
            field=django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
