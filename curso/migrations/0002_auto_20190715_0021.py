# Generated by Django 2.2 on 2019-07-15 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submodulo',
            options={'ordering': ('numero',), 'verbose_name': 'SubMódulo', 'verbose_name_plural': 'SubMódulos'},
        ),
        migrations.AlterField(
            model_name='curso',
            name='nombre',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre del Curso'),
        ),
        migrations.AlterField(
            model_name='submodulo',
            name='modulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.Modulo', verbose_name='Seleccione el Módulo al que pertenece'),
        ),
        migrations.AlterField(
            model_name='submodulo',
            name='numero',
            field=models.IntegerField(verbose_name='SubMódulo'),
        ),
    ]
