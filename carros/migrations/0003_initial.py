# Generated by Django 4.1.1 on 2022-09-14 21:21

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carros', '0002_delete_carro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=12, unique=True)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('ano', models.CharField(max_length=5)),
                ('cor', models.CharField(max_length=50)),
                ('foto', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/carPhotos'), upload_to='')),
            ],
        ),
    ]
