from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'enterprises/home.html')


def details(request, enterprise_id):
    return render(request, 'enterprises/details.html')
