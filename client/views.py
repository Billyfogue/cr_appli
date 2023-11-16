from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Client
from commande.filters import CommandeFiltre
from django.contrib.auth.decorators import login_required
from .forms import ClientForm
# Create your views here.

@login_required(login_url='acces')
def list_client(request,pk):
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    commande_total=commande.count()
    myFilter=CommandeFiltre(request.GET,queryset=commande)
    commande=myFilter.qs



    context={'client':client,'commande':commande,'commande_total':commande_total,'myFilter':myFilter}
    return render(request,'client/list_client.html',context)

def ajouter_client(request):
    form=ClientForm()
    if request.method=='POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'client/ajout_client.html',context)

def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'client/liste_client.html', {'clients': clients})



#cette partie doit etre comme ca au cas ou ca ne marche pas (les 2 premiere lignes de code )
#from django.shortcuts import render,HttpResponse
