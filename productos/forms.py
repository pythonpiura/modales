from django import forms
from django.forms.models import modelformset_factory, inlineformset_factory
from productos.models import Producto, Proveedor, Compra, DetalleCompra


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

class CompraForm(forms.ModelForm):

    class Meta:
        model = Compra
        fields = ['proveedor']

    def __init__(self, *args, **kwargs):
        super(CompraForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

class DetalleCompraForm(forms.ModelForm):

    class Meta:
        model = DetalleCompra
        fields = ['producto','cantidad','precio_compra']

    def __init__(self, *args, **kwargs):
        super(DetalleCompraForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad == '':
            raise forms.ValidationError("Debe ingresar una cantidad valida")
        return cantidad

    def clean_precio_compra(self):
        precio = self.cleaned_data['precio_compra']
        if precio == '':
            raise forms.ValidationError("Debe ingresar un precio valido")
        return precio

DetalleCompraFormSet = inlineformset_factory(Compra, DetalleCompra, form=DetalleCompraForm, extra=4)