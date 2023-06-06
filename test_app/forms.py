from django import forms
from django.forms import ModelForm, TextInput, EmailInput
from .models import User, Company, Quotation


class loginForm(forms.Form): 
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control enter_input'}))
    password= forms.CharField(
        max_length=65, 
        widget=forms.PasswordInput(attrs={'class': 'form-control enter_input'}))
    


YEARS = [x for x in range(1940, 1)]

class registerForm(forms.Form):
    companyName = forms.CharField(label = "Nombre de la empresa", max_length = 50, widget = forms.TextInput(attrs={'class': 'form-control enter_input'}))
    
    companyNit = forms.CharField(label = "NIT de la empresa", max_length=9, widget = forms.TextInput(attrs={'class': 'form-control enter_input'}))
    
    companyAddress = forms.CharField(label = "Dirección de la empresa", max_length=300, widget = forms.TextInput(attrs={'class': 'form-control enter_input'}))
    
    companyPhone = forms.CharField(label = "Teléfono de la empresa", max_length=15, widget = forms.TextInput(attrs={'class': 'form-control enter_input'}))
    
    userName = forms.CharField(label = "Nombre del representante", max_length=50, widget = forms.TextInput(attrs={'class': 'form-control enter_input'}))
    
    userCC = forms.CharField(label = "Cédula del representante", max_length=10, widget = forms.TextInput(attrs={'class': 'form-control enter_input'}))
    
    userEmail = forms.EmailField(label = "Email del representante", max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control enter_input'}))
    
    userPassword = forms.CharField(label = "Contraseña de usuairo del representante", max_length=16, widget = forms.TextInput(attrs={'class': 'form-control enter_input'}))
    
    userPhone = forms.CharField(label = "Teléfono del representante", max_length=15, widget = forms.NumberInput(attrs={'class': 'form-control enter_input'}))
    
    #YYY-MMM-DDD
    userBirthday = forms.DateField(label = "Fecha de nacimiento del representante")



class editProfileForm(ModelForm):
    class Meta:
        model=User
        fields=['fullname', 'email', 'phoneNumberU']
        widgets = {
            'fullname': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px; font-size: 17px;'
                }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px; font-size: 17px;'
                }),
            'phoneNumberU': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 500px; font-size: 17px;'
                })
        }

class editCompanyForm(ModelForm):
    class Meta:
        model=Company
        fields=['address', 'phoneNumberC']
        widgets = {
            'address': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px; font-size: 17px;'
                }),
            'phoneNumberC': TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 400px; font-size: 17px;'
                })
        }

class crateMeetingBinacle(forms.Form):
    class Meta:
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
        
        
class editMeetingForm(forms.Form):
    class Meta:
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


class editQuoteForm(ModelForm): 
    class Meta: 
        model=Quotation
        fields=['description', 'price']
        widgets={
            'price': forms.widgets.TextInput(attrs={
                'type':"inputText",
                'class':"form-control",
                'id':"InputText",
                'label': "Precio de la cotización",
                'style':"width: 270px;"
            }),
            'description': forms.widgets.Textarea(attrs={
                'class':"form-control",
                'id':"FormControlTextarea1",
                'rows':"4",
                'label': "Descripción de la cotización",
                'style':"width: 68%;margin-left: 1%"
            })
        }


#class registerForm(forms.Form): 
 #   companyNit = forms.CharField(max_length=9, widget = forms.CharField(attrs={'class': 'form-control enter_input'}))
