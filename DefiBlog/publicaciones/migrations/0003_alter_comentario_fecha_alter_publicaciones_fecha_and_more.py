# Generated by Django 4.2.3 on 2023-07-27 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0002_publicaciones_creador_comentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='publicaciones',
            name='fecha',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='publicaciones',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
