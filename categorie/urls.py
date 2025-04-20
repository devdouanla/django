from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "categorie"
urlpatterns = [

    path('<int:matricule>/', views.home, name='home'),
      path('form/<int:matricule>/', views.formulaire, name='formulaire'),
          path('forme/<int:id>/', views.updateform, name='form'),
       path('ajouter/<int:matricule>/', views.add, name='add'),
      path('delete/<int:id>/', views.delete, name='delete'),
       path('update/<int:id>/', views.update, name='update'),





]