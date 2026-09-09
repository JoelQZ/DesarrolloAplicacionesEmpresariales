from django import forms
from .models import Pizza


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['nombre', 'tipo_masa', 'ingredientes', 'disponible']
        labels = {
            'nombre': 'Nombre de la Pizza',
            'tipo_masa': 'Tipo de Masa',
            'ingredientes': 'Ingredientes',
            'disponible': 'Disponible',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Margarita'
            }),
            'tipo_masa': forms.Select(attrs={
                'class': 'form-select'
            }),
            'ingredientes': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Tomate, queso, albahaca',
                'rows': 4
            }),
            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
