
from django.db import models

class AutomobilioModelis(models.Model):
    marke = models.CharField('Markė', max_length=100)
    modelis = models.CharField('Modelis',max_length=100)

    def __str__(self):
        return f"{self.marke} {self.modelis}"
class Automobilis(models.Model):
    valstybinis_nr = models.CharField('Valstybinis numeris',max_length=100)
    vin_kodas = models.CharField('VIN kodas',max_length=100)
    klientas = models.CharField('Klientas',max_length=100)
    automobilio_modelis = models.ForeignKey(to=AutomobilioModelis, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.automobilio_modelis}({self.valstybinis_nr})"
class Paslauga(models.Model):
    pavadinimas = models.CharField('Pavadinimas', max_length=100)
    kaina = models.FloatField('Kaina')
    def __str__(self):
        return f"{self.pavadinimas}"
class Uzsakymas(models.Model):
    data = models.DateField("Data", auto_now_add=True)
    automobilis = models.ForeignKey("Automobilis", on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.automobilis}({self.data})"
class UzsakymoEilute(models.Model):
    uzsakymas = models.ForeignKey("Uzsakymas", on_delete=models.CASCADE)
    paslauga = models.ForeignKey("Paslauga", on_delete=models.SET_NULL, null=True)
    kiekis = models.IntegerField("Kiekis")
    def __str__(self):
        return f"{self.uzsakymas.data}, {self.paslauga}({self.kiekis})"




