# Generated by Django 2.2 on 2019-08-24 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evaluacion', '0017_auto_20190815_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudianteevaluacion',
            name='estudiante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='curso.EstudianteCurso'),
        ),
    ]
