from django.shortcuts import render
from accounts import views

def homepage(request):
    if request.method == 'POST':
        return views.user_login(request)
    else:
        return render(request, "home.html")

def accountpage(request):
    return render(request, "my_account.html")

def productpage(request):
    return render(request, "product_page.html")

def resultpage(request):
    return render(request, "results.html")

def myfoodpage(request):
    return render(request, "my_food.html")
