# -*- coding: utf-8 -*-
from django import forms
from core import consts as CONST
from core import messages as MSG
import common.models as MODELS
import user.services as SERVICES

class updateUserForm(forms.ModelForm):

    class Meta:
        model = MODELS.CustomUser
        fields = ('gender_style', 'living_country', 'living_area', 'description', 'photo')
        widgets = {
                    'description': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
                    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class replyForm(forms.ModelForm):

    class Meta:
        model = MODELS.Reply
        fields = ('reply', 'comment', 'user', 'date')
        widgets = {
                    'reply': forms.Textarea(attrs={'cols': 80, 'rows': 2}),
                    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
        self.fields['reply'].widget.attrs['placeholder'] = 'この投稿に返信する'
