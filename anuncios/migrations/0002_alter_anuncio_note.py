# Generated by Django 3.2 on 2021-05-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='note',
            field=models.IntegerField(verbose_name='Nota total'),
        ),
    ]
