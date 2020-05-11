# -*- coding: utf-8 -*-
from django import forms
from core import consts as CONST
import common.models as MODELS

class detailSearchForm(forms.ModelForm):

    class Meta:
        model = MODELS.BeerTasteAvg
        widgets = {
            'overall': forms.Select(choices=CONST.EVALUATION_CHOICES_GOODNESS),
            'bitterness': forms.Select(choices=CONST.EVALUATION_CHOICES_STRONGNESS),
            'aroma': forms.Select(choices=CONST.EVALUATION_CHOICES_STRONGNESS),
            'body': forms.Select(choices=CONST.EVALUATION_CHOICES_EXISTNESS),
            'drinkability': forms.Select(choices=CONST.EVALUATION_CHOICES_GOODNESS),
            'pressure': forms.Select(choices=CONST.EVALUATION_CHOICES_STRONGNESS),
            'specialness': forms.Select(choices=CONST.EVALUATION_CHOICES_EXISTNESS),
        }

        fields = ("bitterness", "aroma", "body", "drinkability", "pressure", "specialness", "overall")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
