from django import forms
from .models import *
from django.core.exceptions import ValidationError


class AddCatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['coll'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Cat
        fields = ['name', 'slug', 'content', 'photo', 'is_published', 'coll']
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-input'}),
                'slug': forms.TextInput(attrs={'class': 'form-input'}),
                'content': forms.Textarea(attrs={'cols': 60, 'rows': 10})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 200:
            raise ValidationError('Длинна превышает 200 символов')

        return name
