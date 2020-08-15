# -*- coding: utf-8 -*-
from django import forms
from core import consts as CONST
from core import messages as MSG
import common.models as MODELS
import beer.services as SERVICES

"""
class addCommentForm(forms.ModelForm):

    class Meta:
        model = MODELS.Comment
        widgets = {
            'overall': forms.Select(choices=CONST.EVALUATION_ADD_CHOICES_GOODNESS),
            'bitterness': forms.Select(choices=CONST.EVALUATION_ADD_CHOICES_STRONGNESS),
            'aroma': forms.Select(choices=CONST.EVALUATION_ADD_CHOICES_STRONGNESS),
            'body': forms.Select(choices=CONST.EVALUATION_ADD_CHOICES_EXISTNESS),
            'drinkability': forms.Select(choices=CONST.EVALUATION_ADD_CHOICES_GOODNESS),
            'pressure': forms.Select(choices=CONST.EVALUATION_ADD_CHOICES_STRONGNESS),
            'specialness': forms.Select(choices=CONST.EVALUATION_ADD_CHOICES_EXISTNESS),
            'comment': forms.Textarea(),
            'beer': forms.HiddenInput(),
            'venue': forms.HiddenInput(),
            'user':forms.HiddenInput(),
        }

        fields = ("bitterness", "aroma", "body", "drinkability", "pressure", "specialness", "overall", "comment", "beer", "venue", "user")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
"""

class addCommentForm(forms.Form):
    overall = forms.ChoiceField(label='総合', choices=CONST.EVALUATION_ADD_CHOICES_GOODNESS)
    bitterness = forms.ChoiceField(label='苦味', choices=CONST.EVALUATION_ADD_CHOICES_STRONGNESS)
    aroma = forms.ChoiceField(label='香り', choices=CONST.EVALUATION_ADD_CHOICES_STRONGNESS)
    body = forms.ChoiceField(label='ボディ', choices=CONST.EVALUATION_ADD_CHOICES_EXISTNESS)
    drinkability = forms.ChoiceField(label='飲み易さ', choices=CONST.EVALUATION_ADD_CHOICES_GOODNESS)
    pressure = forms.ChoiceField(label='炭酸', choices=CONST.EVALUATION_ADD_CHOICES_STRONGNESS)
    specialness = forms.ChoiceField(label='独自感', choices=CONST.EVALUATION_ADD_CHOICES_EXISTNESS)
    comment = forms.CharField(label='コメント', widget=forms.Textarea(attrs={'rows': '3'}))
    beer_name = forms.CharField(label='ビール名', max_length=200)
    beer_id = forms.CharField(label='ビールid', widget = forms.HiddenInput, required=False)
    brewery_name = forms.CharField(label='ブルワリー名', max_length=200)
    brewery_id = forms.CharField(label='ブルワリーid', widget = forms.HiddenInput, required=False)
    venue_name = forms.CharField(label='店舗名', max_length=200, required=False)
    venue_id = forms.CharField(label='店舗id', widget = forms.HiddenInput, required=False)
    photo = forms.ImageField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    #        field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる
        self.fields['photo'].widget.attrs['class'] = 'custom-file-input'

    def clean_overall(self):
        overall = self.cleaned_data.get('overall')
        if overall == "0":
            self.reset_evaluation_values()
            raise forms.ValidationError(MSG.PLEASE_SELECT)
        return overall

    def clean_bitterness(self):
        bitterness = self.cleaned_data.get('bitterness')
        if bitterness == "0":
            self.reset_evaluation_values()
            raise forms.ValidationError(MSG.PLEASE_SELECT)
        return bitterness

    def clean_aroma(self):
        aroma = self.cleaned_data.get('aroma')
        if aroma == "0":
            self.reset_evaluation_values()
            raise forms.ValidationError(MSG.PLEASE_SELECT)
        return aroma

    def clean_body(self):
        body = self.cleaned_data.get('body')
        if body == "0":
            self.reset_evaluation_values()
            raise forms.ValidationError(MSG.PLEASE_SELECT)
        return body

    def clean_drinkability(self):
        drinkability = self.cleaned_data.get('drinkability')
        if drinkability == "0":
            self.reset_evaluation_values()
            raise forms.ValidationError(MSG.PLEASE_SELECT)
        return drinkability

    def clean_pressure(self):
        pressure = self.cleaned_data.get('pressure')
        if pressure == "0":
            self.reset_evaluation_values()
            raise forms.ValidationError(MSG.PLEASE_SELECT)
        return pressure

    def clean_specialness(self):
        specialness = self.cleaned_data.get('specialness')
        if specialness == "0":
            self.reset_evaluation_values()
            raise forms.ValidationError(MSG.PLEASE_SELECT)
        return specialness

    def reset_evaluation_values(self):
        self.data = self.data.copy()
        self.data['overall'] = 0
        self.data['bitterness'] = 0
        self.data['aroma'] = 0
        self.data['body'] = 0
        self.data['drinkability'] = 0
        self.data['pressure'] = 0
        self.data['specialness'] = 0
        return

    def clean(self):
        cleaned_data = super(addCommentForm, self).clean()
        beer_name = self.cleaned_data.get('beer_name')
        beer_id = self.cleaned_data.get('beer_id')
        brewery_name = self.cleaned_data.get('brewery_name')
        brewery_id = self.cleaned_data.get('brewery_id')
        venue_name = self.cleaned_data.get('venue_name')
        venue_id = self.cleaned_data.get('venue_id')

        """
        if beer_id:
            beer = SERVICES.selectBeerById(beer_id)
            if beer_name != beer.name:
                raise forms.ValidationError(MSG.UNMATCH_BEER_NAME_AND_BEER_ID)

        if brewery_id:
            brewery = SERVICES.selectBreweryById(brewery_id)
            if brewery_name != brewery.name:
                raise forms.ValidationError(MSG.UNMATCH_BREWERY_NAME_AND_BREWERY_ID)

        if brewery_id and beer_id:
            beer = SERVICES.selectBeerById(beer_id)
            if str(brewery_id) != str(beer.brewery.id):
                raise forms.ValidationError(MSG.UNMATCH_BREWERY_AND_BEER)

        if beer_id and not brewery_id:
            beer = SERVICES.selectBeerById(beer_id)
            if beer.brewery.name != brewery_name:
                raise forms.ValidationError(MSG.UNMATCH_BEER_ID_AND_BREWERY_NAME)

        if venue_id:
            venue = SERVICES.selectVenueById(venue_id)
            if venue.name != venue_name:
                raise forms.ValidationError(MSG.UNMATCH_VENUE_ID_AND_VENUE_NAME)
        """
        return cleaned_data
