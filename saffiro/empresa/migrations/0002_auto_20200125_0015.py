# Generated by Django 2.2.3 on 2020-01-25 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='direccion',
            field=models.CharField(max_length=20, null=True, verbose_name='Direccion'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='telefono',
            field=models.CharField(max_length=20, null=True, verbose_name='Telefono'),
        ),
    ]
