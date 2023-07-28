# Generated by Django 4.2.3 on 2023-07-27 20:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('publicaciones', '0003_alter_comentario_fecha_alter_publicaciones_fecha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='meGusta',
            field=models.ManyToManyField(blank=True, related_name='comentarios_gustados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicaciones',
            name='meGusta',
            field=models.ManyToManyField(blank=True, related_name='publicaciones_gustadas', to=settings.AUTH_USER_MODEL),
        ),
    ]