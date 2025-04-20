from django.db import models
from gestionnaire.models import Gestionnaire
# Create your models here.
class Quartier(models.Model):
    id = models.BigAutoField(primary_key=True)  # <== CORRECT ICI
    nom = models.CharField(max_length=100, default="blue")
    description =models.TextField()
    surperficie =models.FloatField()
    gestionnaire =  models.ForeignKey(Gestionnaire,on_delete=models.CASCADE)

    def reste_surface(self):
        r=self.surperficie
        return r-int(self.maison_set.aggregate(total_surface=models.Sum('surperficie'))['total_surface'] or 0)

    

    

