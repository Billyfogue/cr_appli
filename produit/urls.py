
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='acceuil'),
    path('list_produit/',views.list_produit,name='list_produit'),
    path('ajout_produit/',views.ajout_produit,name='ajout_produit'),
]