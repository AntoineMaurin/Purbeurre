from django.urls import path
from actions import views

urlpatterns = [
    path('results', views.search),
]
