from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('pw1')
            password2 = form.cleaned_data.get('pw2')

            if User.objects.filter(email=email).exists():
                messages.error(request, "Cet email est déjà utilisé.")
                form = UserRegisterForm(request.POST)
                return render(request, "registration.html", {'form': form})
            elif password1 != password2:
                messages.error(request, "Les mots de passe ne correspondent"
                               " pas.")
                form = UserRegisterForm(request.POST)
                return render(request, "registration.html", {'form': form})
            elif len(password1) < 6:
                messages.warning(request, "Ce mot de passe est trop court,"
                                " il doit comporter au moins 6 caractères.")
                form = UserRegisterForm(request.POST)
                return render(request, "registration.html", {'form': form})
            else:
                user = User.objects.create_user(username=email,
                                                email=email,
                                                password=password1)
                # username = email.split("@")[0]
                messages.success(request, "Compte créé ! "
                                 "Bienvenue {}".format(email))
                form = UserLoginForm()
                return render(request, "login.html", {'form': form})

    else:
        form = UserRegisterForm()
        return render(request, "registration.html", {'form': form})

def user_login(request):
    form = UserLoginForm(request.POST)
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return render(request, "home.html", {'user': user})
        else:
            messages.error(request, "Email ou mot de passe incorrect.")
            return render(request, "login.html", {'form': form})
    else:
        form = UserLoginForm()
        return render(request, "login.html", {'form': form})

def user_logout(request):
    logout(request)
    form = UserLoginForm()
    return render(request, "login.html", {'form': form})
