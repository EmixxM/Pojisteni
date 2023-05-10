from django.db import models

# Create your models here.

class Pojisteny(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    email = models.EmailField()
    cislo_popisne = models.CharField(max_length=10)
    telefon = models.CharField(max_length=20)
    ulice = models.CharField(max_length=100)
    psc = models.CharField(max_length=10)
    mesto = models.CharField(max_length=100)
    
    def __str__(self):
        return self.jmeno + ' ' + self.prijmeni



class Pojisteni(models.Model):
    pojisteny_objekt = models.ForeignKey(Pojisteny, on_delete=models.CASCADE, related_name='pojisteni_set')
    nazev = models.CharField(max_length=100, blank=True)
    castka = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    predmet = models.CharField(max_length=100, blank=True)
    platnost_od = models.DateField(blank=True, null=True)
    platnost_do = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'pojisteni'

    def __str__(self):
        return f'Pojisteni číslo {self.id} - {self.predmet}'

