
from django.shortcuts import render, redirect
from .models import Gestionnaire
from categorie.models import Categorie
from quartier.models import Quartier
from maison.models import Maison

from django.db.models import Q
def dashboard(request, matricule):
      gestionnaires = Gestionnaire.objects.get( pk=matricule)
      nb_categories = Categorie.objects.filter(gestionnaire=gestionnaires).count()
      nb_maisons = Maison.objects.filter(gestionnaire=gestionnaires).count()
      nb_quartiers =Quartier.objects.filter(gestionnaire=gestionnaires).count()
      ajouter="ajouter"
      contexte ={"gestionnaire": gestionnaires, "nb_categories": nb_categories, "nb_maisons":  nb_maisons, "nb_quartiers": nb_quartiers}
      return render(request, 'gestionnaire/dashboard.html',contexte)
def login_view(request): 
    username = request.POST.get('username')
    password = request.POST.get('password') 
    gestionnaire = Gestionnaire.objects.filter( Q(email= username)|Q(nom= username), password=password).first()
   

    if gestionnaire:
            # Tu peux enregistrer l'ID en session ou rediriger
             matricule = gestionnaire.matricule
             return dashboard(request, matricule)
  
    else:
         error = "Identifiant ou mot de passe incorrect."

    return render(request, 'gestionnaire/login.html', {"error": error})
# Create your views here.
