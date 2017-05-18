from django.conf.urls import url
from productos.views import ListadoProductos, CrearProducto, ModificarProducto, DetalleProducto

urlpatterns = [
    url(r'^$', ListadoProductos.as_view(), name="listado_productos"),
    url(r'^crear_producto/$', CrearProducto.as_view(), name="crear_producto"),
    url(r'^modificar_producto/(?P<pk>.+)/$',ModificarProducto.as_view(), name="modificar_producto"),
    url(r'^detalle_producto/(?P<pk>.+)/$',DetalleProducto.as_view(), name="detalle_producto"),
]