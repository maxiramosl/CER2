# Generated by Django 4.2.6 on 2023-10-22 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CER2', '0003_comunicado_detalle_comunicado_detalle_corto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicado',
            name='detalle',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='detalle_corto',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='modificado_por',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='publicado_por',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='comunicado',
            name='titulo',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='entidad',
            name='nombre',
            field=models.CharField(default='', max_length=30),
        ),
    ]
