# -*- coding: utf-8 -*-
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from core import consts as CONST
import common.models as MODELS

class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class SignUpForm(UserCreationForm):
    class Meta:
        model = MODELS.CustomUser
        widgets = {
            'birthday': forms.SelectDateWidget(years=[x for x in range(1950, 2020)])
        }
        fields = ("username", "password1", "password2", "email", "birthday", "gender_style")

    # 入力したパスワードの検証(バリデーション)を行っています
    def clean_password(self):
        # 入力されたパスワードを取得します
        password = self.cleaned_data.get('password1')
        # 数字とアルファベットが含まれているのかチェックします。
        if not re.search(r'\d', password):
            raise forms.ValidationError('数字が含まれていません')
        if not re.search(r'[a-zA-Z]', password):
            raise forms.ValidationError('アルファベットが含まれていません')
        return password
