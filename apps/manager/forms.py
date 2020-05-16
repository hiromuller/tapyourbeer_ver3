# -*- coding: utf-8 -*-
from django import forms
from core import consts as CONST
from core import messages as MSG
import common.models as MODELS
import manager.services as SERVICES

class updateBeerForm(forms.ModelForm):

    class Meta:
        model = MODELS.Beer
        fields = ('name', 'style', 'description', 'ibu', 'abv')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class updateBreweryForm(forms.ModelForm):

    class Meta:
        model = MODELS.Brewery
        fields = ('name', 'address', 'description', 'web', 'webshop')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class updateVenueForm(forms.ModelForm):

    class Meta:
        model = MODELS.Venue
        fields = ('name', 'address', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

class mergeBreweryForm(forms.Form):
    base_brewery_id = forms.CharField(label='ベースとなるブルワリー', max_length=200)
    merging_brewery_id = forms.CharField(label='統合して消えるブルワリー', max_length=200)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

    def clean_base_brewery_id(self):
        base_brewery_id = self.cleaned_data.get('base_brewery_id')
        if base_brewery_id:
            is_brewery_exist = SERVICES.is_brewery_exist(base_brewery_id)
            if not is_brewery_exist:
                raise forms.ValidationError(MSG.BREWERY_DOES_NOT_EXIST)
        return base_brewery_id

    def clean_merging_brewery_id(self):
        merging_brewery_id = self.cleaned_data.get('merging_brewery_id')
        if merging_brewery_id:
            is_brewery_exist = SERVICES.is_brewery_exist(merging_brewery_id)
            if not is_brewery_exist:
                raise forms.ValidationError(MSG.BREWERY_DOES_NOT_EXIST)
        return merging_brewery_id


    def clean(self):
        cleaned_data = super(mergeBreweryForm, self).clean()
        base_brewery_id = self.cleaned_data.get('base_brewery_id')
        merging_brewery_id = self.cleaned_data.get('merging_brewery_id')

        if base_brewery_id == merging_brewery_id:
            raise forms.ValidationError(MSG.SAME_VALUE_INPUT)

        return cleaned_data

class mergeBeerForm(forms.Form):
    base_beer_id = forms.CharField(label='ベースとなるビール', max_length=200)
    merging_beer_id = forms.CharField(label='統合して消えるビール', max_length=200)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる

    def clean_base_beer_id(self):
        base_beer_id = self.cleaned_data.get('base_beer_id')
        if base_beer_id:
            is_beer_exist = SERVICES.is_beer_exist(base_beer_id)
            if not is_beer_exist:
                raise forms.ValidationError(MSG.BEER_DOES_NOT_EXIST)
        return base_beer_id

    def clean_merging_beer_id(self):
        merging_beer_id = self.cleaned_data.get('merging_beer_id')
        if merging_beer_id:
            is_beer_exist = SERVICES.is_beer_exist(merging_beer_id)
            if not is_beer_exist:
                raise forms.ValidationError(MSG.BEER_DOES_NOT_EXIST)
        return merging_beer_id


    def clean(self):
        cleaned_data = super(mergeBeerForm, self).clean()
        base_beer_id = self.cleaned_data.get('base_beer_id')
        merging_beer_id = self.cleaned_data.get('merging_beer_id')

        if base_beer_id == merging_beer_id:
            raise forms.ValidationError(MSG.SAME_VALUE_INPUT)

        return cleaned_data
