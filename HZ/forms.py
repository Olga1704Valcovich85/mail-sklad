from  .models import Articl, own_production
from  django.forms import ModelForm, TextInput, DateTimeInput, Textarea, NumberInput


class ArticlForm(ModelForm):
    class Meta:
        model = Articl
        fields = ['title', 'anons', 'full', 'date']

        widgets = {
            'title':TextInput(attrs={
                'class':'form-control',
                'placeholder':"Название публикации",
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Анонс",
            }),
            'full': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Статья",
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата",

            })
        }

class Own_productionForm(ModelForm):
    class Meta:
        model = own_production
        fields = ['name', 'articul', 'kod', 'kolichestvo', 'color', 'size','gender']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Название продукции",
            }),
            'articul': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Артикул",
            }),
            'kod': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Код",
            }),
            'kolichestvo': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Количество",
            }),
            'color': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Цвет",
            }),
            'size': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "Размер",
            }),
            'gender': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Пол",
            }),
        }







