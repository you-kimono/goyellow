from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .models import Enterprise


# Create your views here.
def home_page(request):
    return render(request, 'enterprises/home.html')


def index(request):
    enterprises = Enterprise.objects.all()
    context = {'enterprises' : enterprises, }
    return render(request, 'enterprises/enterprises.html', context)


def details(request, pk):
    enterprise = get_object_or_404(Enterprise, pk=pk)
    context = {'enterprise' : enterprise,}
    return render(request, 'enterprises/details.html', context)


def new_enterprise(request):
    if request.method == 'POST':
        enterprise_name = request.POST['enterprise_name']
        enterprise = Enterprise()
        enterprise.enterprise_name = enterprise_name
        enterprise.save()
        return HttpResponseRedirect(reverse_lazy('enterprises:details', kwargs={'pk':enterprise.id}))
    return render(request, 'enterprises/new.html')
