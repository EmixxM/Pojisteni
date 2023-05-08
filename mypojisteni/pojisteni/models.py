from django.db import models

# Create your models here.

class Pojisteny(models.Model):
    jmeno = models.CharField(max_length=100)
    prijmeni = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.jmeno + ' ' + self.prijmeni

class Pojisteni(models.Model):
    nazev = models.CharField(max_length=100)
    popis = models.TextField()
    pojisteny = models.ForeignKey(Pojisteny, on_delete=models.CASCADE, related_name='pojisteni')
    
    def __str__(self):
        return self.nazev
