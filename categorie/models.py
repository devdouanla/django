from django.db import models
from gestionnaire.models import Gestionnaire


# Create your models here.
class Categorie(models.Model):
      id = models.BigAutoField(primary_key=True)  # <== CORRECT ICI
      nom = models.CharField(max_length=100, default="blue")
      gestionnaire = models.ForeignKey( Gestionnaire,on_delete=models.CASCADE)