
from django import forms
from .models import Pojisteny
from .models import Pojisteni


class PojistenyForm(forms.ModelForm):
    class Meta:
        model = Pojisteny
        fields = ['jmeno', 'prijmeni', 'email', 'telefon', 'ulice', 'cislo_popisne', 'mesto', 'psc']


class PojisteniForm(forms.ModelForm):
    class Meta:
        model = Pojisteni
        fields = ['nazev', 'popis', 'pojisteny']
