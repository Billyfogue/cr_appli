from django.shortcuts import render, HttpResponse, redirect
from commande.models import Commande
from client.models import Client
from produit.models import Produit
from .forms import ProduitForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='acces')
def home(request):
    commandes=Commande.objects.all()
    clients=Client.objects.all()
    context={'commandes':commandes,'clients':clients}
    return render(request,'produit/Acceuil.html',context)


def list_produit(request):
    produits = Produit.objects.all()
    context = {'produits':produits}
    return render(request, 'produit/list_produit.html', context)

def ajout_produit(request):
    form=ProduitForm()
    if request.method=='POST':
        form=ProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'produit/ajout_produit.html',context)