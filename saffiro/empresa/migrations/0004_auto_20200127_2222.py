# Generated by Django 2.2.3 on 2020-01-28 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0003_empresa_removed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresa',
            options={'ordering': ['-creacion'], 'verbose_name': 'Empresa', 'verbose_name_plural': 'Empresas'},
        ),
        migrations.RenameField(
            model_name='empresa',
            old_name='removed',
            new_name='disable',
        ),
    ]
