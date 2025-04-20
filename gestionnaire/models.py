from django.db import models


class Gestionnaire(models.Model):
    matricule = models.BigAutoField(primary_key=True)  # <== CORRECT ICI
    nom = models.CharField(max_length=100, default="blue")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, default="blue")
    # Create your models here.
