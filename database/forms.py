from django import forms

class UserRegisterForm(forms.Form):
    mail = forms.CharField(label='Email : ', max_length=100)
    password = forms.CharField(max_length=50)
