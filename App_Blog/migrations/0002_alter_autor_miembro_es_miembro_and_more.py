# Generated by Django 4.0.6 on 2022-09-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor_miembro',
            name='es_miembro',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='fecha',
            field=models.DateField(),
        ),
    ]