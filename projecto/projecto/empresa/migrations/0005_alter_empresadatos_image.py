# Generated by Django 5.0 on 2023-12-11 18:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_alter_empresadatos_options_alter_empresadatos_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresadatos',
            name='image',
            field=models.ImageField(default=datetime.datetime(2023, 12, 11, 18, 38, 45, 320645, tzinfo=datetime.timezone.utc), upload_to='projectempresa', verbose_name='Imagen'),
            preserve_default=False,
        ),
    ]
