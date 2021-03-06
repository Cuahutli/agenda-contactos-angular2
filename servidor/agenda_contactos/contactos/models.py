from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = (
        ('M', 'Hombre'),
        ('F', 'Mujer'),
)

class Contacto(models.Model):
    nombre = models.CharField(null=False, blank=False, max_length=255)
    primer_apellido = models.CharField(null=False, blank=True, max_length=255)
    segundo_apellido = models.CharField(null=False, blank=True, max_length=255)
    fecha_nacimiento = models.DateField(null=False, blank=True)
    telefono_fijo = models.CharField(null=False, blank=True, max_length=255)
    telefono_movil = models.CharField(null=False, blank=True, max_length=255)
    puesto = models.CharField(null=False, blank=True, max_length=255)
    genero = models.CharField(null=False, blank=True, choices=GENDER_CHOICES, max_length=255)
    direccion = models.CharField(null=False, blank=True, max_length=255)
    email = models.EmailField(null=True, blank=True)
    imagen = models.ImageField(null=True, blank=True)

    propietario = models.ForeignKey(User, null=True, blank=True)
    borrado = models.BooleanField(default=False)



