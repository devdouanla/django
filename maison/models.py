from django.db import models
from quartier.models import Quartier
from categorie.models import Categorie

from gestionnaire.models import Gestionnaire

# Create your models here.
class Maison(models.Model):
    id = models.BigAutoField(primary_key=True)  # <== CORRECT ICI
    adresse = models.CharField(max_length=100, default="blue",unique=True)
    surperficie =models.FloatField()
    quartier =  models.ForeignKey(Quartier,on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    gestionnaire =  models.ForeignKey(Gestionnaire,on_delete=models.CASCADE)
