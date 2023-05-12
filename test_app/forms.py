from django import forms
from django.forms import ModelForm, TextInput, EmailInput
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
        widgets = {
            'fullname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; padding:left;'
                }),
            'phoneNumberU': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                })
        }

class editCompanyForm(ModelForm):
    class Meta:
        model=Company
        fields=['address', 'phoneNumberC']
        widgets = {
            'address': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                }),
            'phoneNumberC': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                })
        }

class crateMeetingBinacle(forms.Form):
    class Mera:
        fields=['date', 'hour', 'summary']
        widgets={
            'date': forms.widgets.DateInput(attrs={
                'type':"date",
               'class':"form-control",
               'id':"InputDate",
               'style':"width: 270px;"
            }),
            'hour': forms.widgets.TimeInput(attrs={
                'type':"time",
                'step':"7200",
                'list':"time_list",
                'class':"form-control",
                'id':"InputTime",
                'style':"width: 270px;"
            })
        }
#class registerForm(forms.Form): 
 #   companyNit = forms.CharField(max_length=9, widget = forms.CharField(attrs={'class': 'form-control enter_input'}))
