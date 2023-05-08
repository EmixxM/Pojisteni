
from django import forms
from .models import Pojisteny


class PojistenyForm(forms.ModelForm):
    class Meta:
        model = Pojisteny
        fields = ['jmeno', 'prijmeni', 'email', 'telefon', 'ulice', 'cislo_popisne', 'mesto', 'psc']
