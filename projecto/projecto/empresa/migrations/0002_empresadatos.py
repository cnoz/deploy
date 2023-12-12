# Generated by Django 5.0 on 2023-12-11 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpresaDatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEmpresa', models.CharField(max_length=100, verbose_name='Titulo')),
                ('ubicacion', models.CharField(max_length=100, verbose_name='Ubicacion')),
                ('descripcionEmpresa', models.TextField(max_length=200, verbose_name='Descripcion')),
                ('puestoBuscado', models.CharField(max_length=200, verbose_name='Puesto buscado')),
                ('requisitos', models.TextField()),
                ('beneficios', models.TextField()),
                ('image', models.ImageField(upload_to='projectempresa', verbose_name='Imagen')),
                ('creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
            ],
        ),
    ]