# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=100, unique=True)
    marca = models.CharField(max_length=40,blank=True)
    precio = models.DecimalField(max_digits=15, decimal_places=5, default=0)
    estado = models.BooleanField(default=True)