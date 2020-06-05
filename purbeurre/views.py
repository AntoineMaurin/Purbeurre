from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from accounts import views

def homepage(request):
    return render(request, "home.html", )

@login_required
def accountpage(request):
    return render(request, "my_account.html")

@login_required
def myfoodpage(request):
    return render(request, "my_food.html")

def productpage(request):
    return render(request, "product_page.html")

def resultpage(request):
    return render(request, "results.html")
