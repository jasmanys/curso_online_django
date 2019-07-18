# Generated by Django 2.2 on 2019-07-18 01:34

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0002_auto_20190715_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submodulo',
            name='texto',
        ),
        migrations.AddField(
            model_name='submodulo',
            name='contenido',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=None, max_length=10000, verbose_name='Contenido'),
            preserve_default=False,
        ),
    ]
