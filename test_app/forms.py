from django import forms
from django.forms import ModelForm
from .models import User, Company


class loginForm(forms.Form): 
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control enter_input'}))
    password= forms.CharField(
        max_length=65, 
        widget=forms.PasswordInput(attrs={'class': 'form-control enter_input'}))
    
class editProfileForm(ModelForm):
    class Meta:
        model=User
        fields=['fullname', 'email', 'phoneNumberU']

class editCompanyForm(ModelForm):
    class Meta:
        model=Company
        fields=['address', 'phoneNumberC']

#class registerForm(forms.Form): 
 #   companyNit = forms.CharField(max_length=9, widget = forms.CharField(attrs={'class': 'form-control enter_input'}))
