# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import UpdateView, CreateView
from django.shortcuts import render
from django.views.generic.list import ListView
from django.http.response import HttpResponseRedirect
from productos.forms import ProductoForm
from productos.models import Producto
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView

class ListadoProductos(ListView):
    model = Producto
    template_name = 'productos.html'
    context_object_name = 'productos'

class CrearProducto(CreateView):
    template_name = 'producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listado_productos')

class ModificarProducto(UpdateView):
    model = Producto
    template_name = 'producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listado_productos')


class DetalleProducto(DetailView):
    model = Producto
    template_name = 'detalle_producto.html'