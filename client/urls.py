from django.urls import path
from . import views

urlpatterns = [

    path('/<str:pk>', views.list_client, name='client'),
]



#suprimer uniquement le 1er client au cas ou ca ne marche pas
