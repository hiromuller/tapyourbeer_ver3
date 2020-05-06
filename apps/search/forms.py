# -*- coding: utf-8 -*-
from django import forms
from core import consts as CONST
from core import messages as MSG
import search.services as SERVICES

class searchForm(forms.Form):
    keyword = forms.CharField(label='キーワード', max_length=200)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        #    field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
        self.fields['keyword'].widget.attrs['class'] = 'searchBox'
