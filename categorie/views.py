from django.shortcuts import render,redirect
from gestionnaire.models import Gestionnaire
from .models import Categorie
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def home(request,matricule):
      gestionnaires = Gestionnaire.objects.get( pk=matricule)
      categories = Categorie.objects.filter(gestionnaire=gestionnaires)
      contexte ={ 'categories': categories ,'matricule':matricule}
      return render( request ,'categorie/home.html',contexte )
def formulaire(request,matricule):
      add ="ajouter"
      action="Ajouter"
      contexte ={ 'matricule':matricule ,'add':add  ,'action':action}
      return render( request ,'categorie/form.html',contexte )



def add(request,matricule):
       name = request.POST.get('nom_categorie')
       gestionnaires = Gestionnaire.objects.get( pk=matricule)
       categorie = Categorie( nom=name,gestionnaire=gestionnaires)
       url = reverse('categorie:home', args=[matricule])
       categorie.save()
       return redirect(url)
def delete(request,id):
       categorie =Categorie.objects.get( pk=id)
       matricule= categorie.gestionnaire.matricule
       url = reverse('categorie:home', args=[matricule])
       categorie.delete()
       return redirect(url)
def updateform (request ,id) :
      add ="update"
      action="Modifier"
      categorie =Categorie.objects.get( pk=id)
      contexte ={ 'matricule':id ,'add':add , 'nom': categorie.nom  ,'action':action}
      return render( request ,'categorie/form.html',contexte )
   
       
def update(request,id):
       name = request.POST.get('nom_categorie')
       categorie = Categorie.objects.get(pk=id)
       matricule= categorie.gestionnaire.matricule
       url = reverse('categorie:home', args=[matricule])
       categorie.nom=name
       categorie.save()
       return redirect(url)        
      
      