# Generated by Django 3.2 on 2021-05-16 11:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0010_alter_curso_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curso',
            name='alumnos_id',
        ),
        migrations.AddField(
            model_name='anuncio',
            name='cuso_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='anuncios.curso', verbose_name='Curso'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='estate',
            field=models.CharField(choices=[('publico', 'Publico'), ('oculto', 'Oculto')], default='oculto', max_length=15),
        ),
    ]
