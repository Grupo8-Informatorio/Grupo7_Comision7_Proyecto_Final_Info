# Generated by Django 4.2.3 on 2023-08-02 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0004_comentario_megusta_publicaciones_megusta'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaciones',
            name='imagen_post',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_post'),
        ),
    ]
