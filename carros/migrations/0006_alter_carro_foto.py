# Generated by Django 4.1.1 on 2022-09-16 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0005_alter_carro_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='foto',
            field=models.ImageField(upload_to='media/carPhotos'),
        ),
    ]
