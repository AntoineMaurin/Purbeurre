from django.shortcuts import render
from purbeurre.models import Product, Category

def search(request):
    search = request.GET['search']
    return render(request, "results.html", {'search': search})
