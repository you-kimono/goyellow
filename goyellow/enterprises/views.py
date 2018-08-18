from django.shortcuts import render
from .models import Enterprise


# Create your views here.
def home_page(request):
    return render(request, 'enterprises/home.html')


def enterprises_list(request):
    enterprises = Enterprise.objects.all()
    context = {'enterprises' : enterprises, }
    return render(request, 'enterprises/enterprises.html', context)


def details(request, enterprise_id):
    enterprise = Enterprise.objects.get(pk = enterprise_id)
    context = {'enterprise' : enterprise,}
    return render(request, 'enterprises/details.html', context)
