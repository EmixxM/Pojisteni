
from django import forms
from .models import Pojisteny, Pojisteni


class PojistenyForm(forms.ModelForm):
    class Meta:
        model = Pojisteny
        fields = ['jmeno', 'prijmeni', 'email', 'telefon', 'ulice', 'cislo_popisne', 'mesto', 'psc']


class PojisteniForm(forms.ModelForm):
    class Meta:
        model = Pojisteni
        fields = ['nazev', 'castka', 'predmet', 'platnost_od', 'platnost_do']
        widgets = {
            'platnost_od': forms.DateInput(attrs={'type': 'date'}),
            'platnost_do': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nazev'].widget.attrs['class'] = 'form-control'
        self.fields['castka'].widget.attrs['class'] = 'form-control'
        self.fields['predmet'].widget.attrs['class'] = 'form-control'

