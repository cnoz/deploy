# Generated by Django 5.0 on 2023-12-11 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0007_alter_empresadatos_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresadatos',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='enlace'),
        ),
    ]
