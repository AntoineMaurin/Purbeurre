from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.user_login, name='register'),
    path('logout', views.user_logout),
]
