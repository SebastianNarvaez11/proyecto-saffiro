# Generated by Django 2.2.3 on 2020-01-25 22:37

from django.db import migrations, models
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_user_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=registration.models.custom_upload_to_user, verbose_name='Foto'),
        ),
    ]
