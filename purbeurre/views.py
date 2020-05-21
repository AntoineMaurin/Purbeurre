from django.shortcuts import render

def homepage(request):
    return render(request, "home.html")

def accountpage(request):
    return render(request, "my_account.html")

def productpage(request):
    return render(request, "product_page.html")

def resultpage(request):
    return render(request, "results.html")

def myfoodpage(request):
    return render(request, "my_food.html")
