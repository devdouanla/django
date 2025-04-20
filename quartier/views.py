from django.shortcuts import render,redirect
from gestionnaire.models import Gestionnaire
from .models import Quartier
from maison.models import Maison
from django.urls import reverse

def home(request,matricule):
      gestionnaires = Gestionnaire.objects.get( pk=matricule)
      categories = Quartier.objects.filter(gestionnaire=gestionnaires)
      contexte ={ 'categories': categories ,'matricule':matricule}
      return render( request ,'quartier/home.html',contexte )
def formulaire(request,matricule):
      add ="ajouter"
      action="Ajouter"
      contexte ={ 'matricule':matricule ,'add':add,'action':action}
      return render( request ,'quartier/form.html',contexte )
def add(request,matricule):
        nom = request.POST.get('nom')
        surface = int (request.POST.get('surface'))
        if surface <0:
            surface = -1*surface 
        description = request.POST.get('description')
        gestionnaires = Gestionnaire.objects.get( pk=matricule)
        quartier = Quartier( nom=nom,surperficie=surface, description=description, gestionnaire=gestionnaires)
        url = reverse('quartier:home', args=[matricule])
        quartier.save()
        return redirect(url)
def delete(request,id):
       quartier =Quartier.objects.get( pk=id)
       matricule= quartier.gestionnaire.matricule
       url = reverse('quartier:home', args=[matricule])
       quartier.delete()
       return redirect(url)
def updateform (request ,id) :
      add ="update"
      action="Modifier"
      categorie =Quartier.objects.get( pk=id)
      contexte ={ 'matricule':id ,'add':add , 'quartier': categorie  ,'action':action}
      return render( request ,'quartier/form.html',contexte )
   
       
def update(request,id):
      nom = request.POST.get('nom')
      surface = request.POST.get('surface')
      description = request.POST.get('description')
      categorie = Quartier.objects.get(pk=id)
      matricule= categorie.gestionnaire.matricule
      url = reverse('quartier:home', args=[matricule])
      categorie.nom=nom
      categorie.description=description 
      if surface <0:
            surface = -1*surface
      categorie.surperficie=surface 
     
      categorie.save()
      return redirect(url)        



def detail (request,id):
     quartier = Quartier.objects.get(pk=id) 
     listeMaisons=Maison.objects.filter(quartier=quartier) 
     contexte ={ 'quartier':quartier,'listeMaisons':listeMaisons}             
     return render( request ,'quartier/detail.html',contexte )  