from django.shortcuts import render,redirect
from gestionnaire.models import Gestionnaire
from .models import Maison
from quartier.models import Quartier
from categorie.models import Categorie
from django.urls import reverse

from django.http import HttpResponse

from gestionnaire.models import Gestionnaire

# Create your views here.
def home(request,matricule):
      gestionnaires = Gestionnaire.objects.get( pk=matricule)
     
  
      categories  = Maison.objects.filter(gestionnaire=gestionnaires)
      contexte ={ 'categories': categories ,'matricule':matricule}
      return render( request ,'maison/home.html',contexte )
def formulaire(request,matricule):
      add ="ajouter"
      gestionnaires = Gestionnaire.objects.get( pk=matricule)
      Listecategories= Categorie.objects.filter(gestionnaire=gestionnaires)
      Listequartiers= Quartier.objects.filter(gestionnaire=gestionnaires)
      action="Ajouter"
      contexte ={ 'matricule':matricule ,'add':add,'Listecategories':Listecategories,'Listequartiers': Listequartiers,'action':action } 
      return render( request ,'maison/form.html',contexte )




def add(request,matricule):
        add ="ajouter"
        action="Ajouter"
        adresse = request.POST.get('adresse')
        quartier_id = request.POST.get('quartier')
        categorie_id = request.POST.get('categorie')
        surface = float(request.POST.get('superficie'))
        if surface <0:
            surface = -1*surface
        categories= Categorie.objects.get(pk=categorie_id)
        insuffisance =False
        notUnique = False
        quartiers= Quartier.objects.get(pk=quartier_id)
        if surface>quartiers.reste_surface():
             insuffisance =True
        
        
        quartiers= Quartier.objects.get(pk=quartier_id)
        if Maison.objects.filter(adresse=adresse).exists():
              notUnique = True
            
        if insuffisance == True or notUnique == True:
              gestionnaires = Gestionnaire.objects.get( pk=matricule)
              Listecategories= Categorie.objects.filter(gestionnaire=gestionnaires)
              Listequartiers= Quartier.objects.filter(gestionnaire=gestionnaires)
              contexte ={ 'insuffisance':insuffisance,'notUnique':notUnique,'add':add,'action':action,'Listecategories':Listecategories,'Listequartiers': Listequartiers,'matricule': matricule}
              return  render( request ,'maison/form.html',contexte )
        else:
                gestionnaires = Gestionnaire.objects.get( pk=matricule)
                maison = Maison( adresse=adresse,surperficie=surface,  categorie=categories , quartier=quartiers, gestionnaire=gestionnaires)
                maison.save()
                url = reverse('maison:home', args=[matricule])
        return   redirect(url)
      

   
   
   
   
def delete(request,id):
       maison =Maison.objects.get( pk=id)
       quartiers= Quartier.objects.get(pk=maison.quartier_id)
       matricule= quartiers.gestionnaire.matricule
       url = reverse('maison:home', args=[matricule])
       maison.delete()
       return   redirect(url)  
        
        
def updateform (request ,id) :
      add ="update"
      action="Modifier"
      categorie =Maison.objects.get( pk=id)
      matricule= categorie.gestionnaire.matricule
      gestionnaires = Gestionnaire.objects.get( pk=matricule)
      Listecategories= Categorie.objects.filter(gestionnaire=gestionnaires)
      Listequartiers = Quartier.objects.filter()
      contexte ={ 'matricule':id ,'add':add , 'maison': categorie  ,'action':action,'Listecategories':Listecategories,'Listequartiers':Listequartiers}
      return render( request ,'maison/form.html',contexte )
   
      
def update(request,id):
      adresse = request.POST.get('adresse')
      quartier_id = request.POST.get('quartier')
      categorie_id = request.POST.get('categorie')
      surface = float(request.POST.get('superficie'))
      if surface <0:
            surface = -1*surface
      categorie= Categorie.objects.get(pk=categorie_id)
      maison = Maison.objects.get(pk=id)
      matricule= categorie.gestionnaire.matricule
      url = reverse('maison:home', args=[matricule])
      maison.adresse=adresse 
      maison.surperficie=surface 
      maison.categorie =Categorie.objects.get(pk=categorie_id)
      maison.quartier=Quartier.objects.get(pk=quartier_id)
      maison.save()
      return redirect(url)  

def detail (request,id):
     maison = Maison.objects.get(pk=id) 
     contexte ={ 'maison':maison}             
     return render( request ,'maison/detail.html',contexte )  
        
        
        
        
        
        
        
#
# quartier.save(),'Listequartiers':Listequartiers