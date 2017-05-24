from django import forms

from productos.models import Producto, Proveedor


class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['descripcion', 'marca', 'precio', 'estado']

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field <> 'estado':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

class ProveedorForm(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ['ruc', 'razon_social', 'direccion', 'telefono','correo', 'estado']

    def __init__(self, *args, **kwargs):
        super(ProveedorForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field <> 'estado':
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })