from django.conf.urls import url
from productos.views import ListadoProductos, CrearProducto, ModificarProducto, DetalleProducto, CrearProveedor, ListadoProveedores, \
    ModificarProveedor, DetalleProveedor

urlpatterns = [
    url(r'^$', ListadoProductos.as_view(), name="listado_productos"),
    url(r'^proveedores/$', ListadoProveedores.as_view(), name="listado_proveedores"),
    url(r'^crear_producto/$', CrearProducto.as_view(), name="crear_producto"),
    url(r'^modificar_producto/(?P<pk>.+)/$',ModificarProducto.as_view(), name="modificar_producto"),
    url(r'^detalle_producto/(?P<pk>.+)/$',DetalleProducto.as_view(), name="detalle_producto"),
    url(r'^crear_proveedor/$', CrearProveedor.as_view(), name="crear_proveedor"),
    url(r'^modificar_proveedor/(?P<pk>.+)/$',ModificarProveedor.as_view(), name="modificar_proveedor"),
    url(r'^detalle_proveedor/(?P<pk>.+)/$',DetalleProveedor.as_view(), name="detalle_proveedor"),
]