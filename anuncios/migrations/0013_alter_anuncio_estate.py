# Generated by Django 3.2 on 2021-05-26 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0012_alter_anuncio_estate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='estate',
            field=models.CharField(choices=[('publico', 'Publico'), ('oculto', 'Oculto')], default='oculto', max_length=15),
        ),
    ]
