# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.list import ListView
from productos.forms import ProductoForm, ProveedorForm
from productos.models import Producto, Proveedor
from django.core.urlresolvers import reverse_lazy
from django.views.generic.detail import DetailView

class ListadoProductos(ListView):
    model = Producto
    template_name = 'productos.html'
    context_object_name = 'productos'

class ListadoProveedores(ListView):
    model = Proveedor
    template_name = 'proveedores.html'
    context_object_name = 'proveedores'

class CrearProducto(CreateView):
    template_name = 'producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listado_productos')

class CrearProveedor(CreateView):
    template_name = 'proveedor.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('productos:listado_proveedores')

class ModificarProducto(UpdateView):
    model = Producto
    template_name = 'producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos:listado_productos')

class ModificarProveedor(UpdateView):
    model = Proveedor
    template_name = 'proveedor.html'
    form_class = ProveedorForm
    success_url = reverse_lazy('productos:listado_proveedores')

class DetalleProducto(DetailView):
    model = Producto
    template_name = 'detalle_producto.html'

class DetalleProveedor(DetailView):
    model = Proveedor
    template_name = 'detalle_proveedor.html'