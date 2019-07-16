# Generated by Django 2.2 on 2019-07-15 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('curso', '0001_initial'),
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnunciadoEvaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.TextField(max_length=250, verbose_name='Enunciado')),
                ('foto', models.CharField(blank=True, max_length=300, verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Enunciado',
                'verbose_name_plural': 'Enunciados',
            },
        ),
        migrations.CreateModel(
            name='OpcionEnunciado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion', models.TextField(max_length=100, verbose_name='Enunciado')),
                ('enunciado_evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evaluacion.EnunciadoEvaluacion', verbose_name='Enunciado Evaluacion')),
            ],
            options={
                'verbose_name': 'Opción del Enunciado',
                'verbose_name_plural': 'Opciones del Enunciado',
            },
        ),
        migrations.CreateModel(
            name='TipoRespuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo de Respuesta',
                'verbose_name_plural': 'Tipos de Respuestas',
            },
        ),
        migrations.CreateModel(
            name='SeleccionMultiple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta', models.BooleanField(verbose_name='Respuesta')),
                ('opcion_enunciado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluacion.OpcionEnunciado')),
            ],
            options={
                'verbose_name': 'Seleccion Multiple',
            },
        ),
        migrations.CreateModel(
            name='RelacionarConcepto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcion_enunciado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluacion.OpcionEnunciado')),
                ('respuesta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fk_respuesta', to='evaluacion.OpcionEnunciado')),
            ],
            options={
                'verbose_name': 'Relacionar Concepto',
                'verbose_name_plural': 'Relacionar Conceptos',
            },
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion_maxima', models.DecimalField(decimal_places=2, max_digits=4)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.Modulo', verbose_name='Modulo')),
            ],
            options={
                'verbose_name': 'Evaluación',
                'verbose_name_plural': 'Evaluaciones',
            },
        ),
        migrations.CreateModel(
            name='EstudianteEvaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.DecimalField(decimal_places=2, max_digits=4)),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estudiante.Estudiante')),
                ('evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evaluacion.Evaluacion')),
            ],
            options={
                'verbose_name': 'Evaluación del Estudiante',
                'verbose_name_plural': 'Evaluaciones de los Estudiantes',
            },
        ),
        migrations.AddField(
            model_name='enunciadoevaluacion',
            name='evaluacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='evaluacion.Evaluacion', verbose_name='Evaluación'),
        ),
        migrations.AddField(
            model_name='enunciadoevaluacion',
            name='submodulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.SubModulo', verbose_name='SubModulo'),
        ),
        migrations.AddField(
            model_name='enunciadoevaluacion',
            name='tipo_respuesta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='evaluacion.TipoRespuesta', verbose_name='Tipo de Respuesta'),
        ),
        migrations.CreateModel(
            name='DetalleEstudianteEvaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion_obtenida', models.DecimalField(decimal_places=2, max_digits=4)),
                ('calificacion_maxima', models.DecimalField(decimal_places=2, max_digits=4)),
                ('enunciado_evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evaluacion.EnunciadoEvaluacion')),
                ('estudiante_evaluacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evaluacion.EstudianteEvaluacion')),
            ],
            options={
                'verbose_name': 'Detalle de la evaluación',
                'verbose_name_plural': 'Detalle de Evaluaciones',
            },
        ),
        migrations.CreateModel(
            name='CalificacionSeleccionMultiple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respuesta_estudiante', models.BooleanField(verbose_name='Respuesta del Estudiante')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estudiante.Estudiante', verbose_name='Estudiante')),
                ('seleccion_multiple', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evaluacion.SeleccionMultiple', verbose_name='Pregunta')),
            ],
            options={
                'verbose_name': 'Calificacion de Seleccion Multiple',
            },
        ),
        migrations.CreateModel(
            name='CalificacionRelacionarConcepto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estudiante.Estudiante', verbose_name='Estudiante')),
                ('relacionar_concepto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evaluacion.RelacionarConcepto', verbose_name='Pregunta')),
                ('respuesta_estudiante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evaluacion.OpcionEnunciado', verbose_name='Respuesta del Estudiante')),
            ],
            options={
                'verbose_name': 'Calificacion Relacionar Concepto',
            },
        ),
    ]
