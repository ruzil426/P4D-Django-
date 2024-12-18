from django import forms

class CityInput(forms.Form):
    city = forms.CharField(max_length=25, label="Город")

