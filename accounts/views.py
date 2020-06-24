from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from accounts.forms import UserRegisterForm, UserLoginForm
from accounts.register_management import RegisterManagement


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('pw1')
            password2 = form.cleaned_data.get('pw2')

            rm = RegisterManagement(email=email, pw1=password1, pw2=password2)
            message = rm.analyze()
            if message[0] == 'error':
                messages.error(request, message[1])
                form = UserRegisterForm(request.POST)
                return render(request, "registration.html", {'form': form})
            else:
                User.objects.create_user(username=email,
                                         email=email,
                                         password=password1)
                messages.success(request, message[1])
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
            request.session['user_mail'] = user.email
            request.session['user_name'] = user.email.split("@")[0]
            return redirect("/")
        else:
            messages.error(request, "Email ou mot de passe incorrect.")
            return render(request, "login.html", {'form': form})
    else:
        form = UserLoginForm()
        return render(request, "login.html", {'form': form})


def user_logout(request):
    logout(request)
    form = UserLoginForm()
    try:
        del request.session['user_mail']
        del request.session['user_name']
    except KeyError:
        pass
    return render(request, "login.html", {'form': form})
