from django.urls import path
from favourites import views

urlpatterns = [
    path('save/<int:id>', views.save),
    path('remove/<int:id>', views.remove),
    path('myfood', views.myfoodpage),
]
