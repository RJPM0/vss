# Generated by Django 3.2 on 2021-05-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0006_auto_20210501_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='estate',
            field=models.CharField(choices=[('oculto', 'Oculto'), ('publico', 'Publico')], default='oculto', max_length=15),
        ),
    ]
