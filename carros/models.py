from django.db import models
from django.core.files.storage import FileSystemStorage

photoCar = FileSystemStorage(location='/media/carPhotos')

# Create your models here.
class Carro(models.Model):
    placa = models.CharField(max_length=12, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano = models.CharField(max_length=5)
    cor = models.CharField(max_length=50)
    foto = models.ImageField(storage=photoCar)