﻿from django.db import models
from django.db.models import Max
from estudiante.models import Estudiante

class Curso(models.Model):
    nombre = models.CharField(verbose_name='Nombre del Curso', max_length=50, unique=True)
    descripcion = models.TextField(verbose_name='Descripción', max_length=600)
    comentario = models.TextField(verbose_name='Comentario', max_length=600)
    icono = models.ImageField(verbose_name='Icono', upload_to='fotos_curso/', null=True, blank=True)


    def __str__(self):
        return "Curso de {}".format(self.nombre)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

class EstudianteCurso(models.Model):
    estudiante = models.ForeignKey(Estudiante, verbose_name='Elija al Estudiante', on_delete=models.PROTECT)
    cursos = models.ManyToManyField(Curso, verbose_name="Cursos")

    def __str__(self):
        return 'Estudiante: {}'.format(self.estudiante.nombres())

    class Meta:
        verbose_name = 'Estudiante del Curso'
        verbose_name_plural = 'Estudiantes del Curso'

class Recurso(models.Model):
    curso = models.ForeignKey(Curso, verbose_name="Curso", on_delete=models.CASCADE)
    descripcion = models.TextField(verbose_name='Descripcion', max_length=600)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

class Item(models.Model):
    descripcion = models.TextField(verbose_name='Descripción', max_length=600)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Item para Recurso'
        verbose_name_plural = 'Items para Recursos'

class RecursoItem(models.Model):
    titulo = models.CharField(verbose_name='Título', max_length=200)
    item = models.ManyToManyField(Item, verbose_name='Item')
    descripcion = models.TextField(verbose_name='Descripción', max_length=600)
    recurso = models.ForeignKey(Recurso, verbose_name='Recurso', on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} - {} - {}'.format(self.titulo, self.item, self.descripcion, self.recurso)

    class Meta:
        verbose_name = 'Item de Recurso'
        verbose_name_plural = 'Items de Recursos'

class Modulo(models.Model):
    numero = models.IntegerField(verbose_name='Numero del Módulo')
    titulo = models.CharField(verbose_name='Título', max_length=200, blank=False, null=False)
    curso = models.ForeignKey(Curso, verbose_name="Curso", on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {} - Curso: {}'.format(self.numero, self.titulo, self.curso)

    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'
        ordering = ('numero',)

    def save(self, *args, **kwargs):
        if not self.id:
            if Modulo.objects.filter(curso__id = self.curso.id).exists():
                mod = Modulo.objects.filter(curso__id = self.curso.id).aggregate(max_numero = Max('numero'))
                self.numero = mod.get('max_numero') + 1
            else:
                self.numero = 1
        else:
            mod = Modulo.objects.get(id=self.id)
            self.numero = mod.numero
        super(Modulo, self).save(*args, **kwargs)

class SubModulo(models.Model):
    numero = models.IntegerField(verbose_name='SubMódulo')
    titulo = models.CharField(verbose_name='Título', max_length=200)
    texto = models.TextField(verbose_name='Contenido', max_length=10000, blank=True)
    modulo = models.ForeignKey(Modulo, verbose_name="Seleccione el Módulo al que pertenece", on_delete=models.CASCADE)

    def __str__(self):
        return '{}.{} - {} - Módulo: {} - Curso: {}'.format(self.modulo.numero, self.numero, self.titulo, self.modulo.titulo, self.modulo.curso.nombre)

    class Meta:
        verbose_name = 'SubMódulo'
        verbose_name_plural = 'SubMódulos'
        ordering = ('numero',)

    def save(self, *args, **kwargs):
        if not self.id:
            if SubModulo.objects.filter(modulo__id = self.modulo.id).exists():
                mod = SubModulo.objects.filter(modulo__id = self.modulo.id).aggregate(max_numero = Max('numero'))
                self.numero = mod.get('max_numero') + 1
            else:
                self.numero = 1
        else:
            mod = SubModulo.objects.get(id=self.id)
            self.numero = mod.numero
        super(SubModulo, self).save(*args, **kwargs)

class Foto(models.Model):
    nombre_foto = models.CharField(verbose_name='Nombre de la foto', max_length=100)
    foto = models.ImageField(verbose_name='Foto', upload_to='fotos/', null=True, blank=True)

    def __str__(self):
        return "Nombre de la foto: {}".format(self.nombre_foto)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

class Video(models.Model):
    nombre_video = models.CharField(verbose_name='Nombre del vídeo', max_length=100)
    link_video = models.TextField(verbose_name='Link el vídeo', max_length=500)

    def __str__(self):
        "Nombre del vídeo: {}".format(self.nombre_video)

    class Meta:
        verbose_name = 'Vídeo'
        verbose_name_plural = 'Vídeos'

class Audio(models.Model):
    nombre_audio = models.CharField(verbose_name='Nombre del audio', max_length=100)
    audio = models.FileField(verbose_name='Audio', upload_to='audios/', null=True, blank=True)

    def __str__(self):
        "Nombre del audio: {}".format(self.nombre_audio)

    class Meta:
        verbose_name = 'Audio'
        verbose_name_plural = 'Audios'

class FotoSubModulo(models.Model):
    sub_modulo = models.ForeignKey(SubModulo, on_delete=models.CASCADE)
    foto = models.ManyToManyField(Foto)

    def __str__(self):
        return self.sub_modulo.titulo

    class Meta:
        verbose_name = 'Foto de SubModulo'
        verbose_name_plural = 'Fotos de SubModulos'

class VideoSubModulo(models.Model):
    sub_modulo = models.ForeignKey(SubModulo, on_delete=models.CASCADE)
    video = models.ManyToManyField(Video)

    def __str__(self):
        return self.sub_modulo.titulo

    class Meta:
        verbose_name = 'Vídeo para SubModulo'
        verbose_name_plural = 'Vídeos para SubModulos'

class AudioSubModulo(models.Model):
    sub_modulo = models.ForeignKey(SubModulo, on_delete=models.CASCADE)
    audio = models.ManyToManyField(Audio)

    def __str__(self):
        return self.sub_modulo.titulo

    class Meta:
        verbose_name = 'Audio para SubModulo'
        verbose_name_plural = 'Audios para SubModulos'
