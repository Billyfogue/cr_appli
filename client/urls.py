from django.urls import path
from . import views

urlpatterns = [

    path('/<str:pk>', views.list_client, name='client'),
    path('ajout_client/', views.ajouter_client,name='ajout_client'),
    path('liste_clients/', views.liste_clients, name='liste_clients'),
]



#suprimer uniquement le 1er client au cas ou ca ne marche pas
