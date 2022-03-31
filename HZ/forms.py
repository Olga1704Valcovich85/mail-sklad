from  .models import Articl, own_production
from  django.forms import ModelForm, TextInput, DateTimeInput, Textarea


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
            # 'date': DateTimeInput(attrs={
            #     'class': 'form-control',
            #     'placeholder': "Дата",

           # })
        }

class Own_productionForm(ModelForm):
    class Meta:
        mod = own_production
        fiel = ['name', 'articul', 'kod', 'kolichestvo', 'color', 'size','gender', 'user_name']



