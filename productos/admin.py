# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from productos.models import Compra, DetalleCompra


class DetalleCompraAdmin(admin.TabularInline):
    model = DetalleCompra

class CompraAdmin(admin.ModelAdmin):
    inlines = [DetalleCompraAdmin]

admin.site.register(Compra, CompraAdmin)




