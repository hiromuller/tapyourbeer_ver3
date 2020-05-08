# -*- coding: utf-8 -*-
from django import forms
from core import consts as CONST
import common.models as MODELS

class updateBeerForm(forms.ModelForm):

    class Meta:
        model = MODELS.Beer
        fields = ('name', 'style', 'description', 'ibu', 'abv')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
