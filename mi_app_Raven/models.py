from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()


    def __str__(self):
        return self.nombre


class vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    legajo = models.CharField(max_length=100)


    def __str__(self):
        return self.nombre
