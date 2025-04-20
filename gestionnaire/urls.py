from django.contrib import admin
from django.urls import path,include
from . import views
app_name = "gestionnaire"
urlpatterns = [
 
    path('', views.login_view, name='login'),
    
  path('dashboard/<int:matricule>/', views.dashboard, name='dashboard'),
  ]




