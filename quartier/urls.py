from . import views
from django.urls import path,include

app_name = "quartier"
urlpatterns = [

    path('<int:matricule>/', views.home, name='home'),
      path('form/<int:matricule>/', views.formulaire, name='formulaire'),
       path('forme/<int:id>/', views.updateform, name='form'),
      path('ajouter/<int:matricule>/', views.add, name='add'),
     path('delete/<int:id>/', views.delete, name='delete'),
     path('update/<int:id>/', views.update, name='update'),
     path('detail/<int:id>/', views.detail, name='detail'),

     





]