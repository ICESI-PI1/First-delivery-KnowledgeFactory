from django import forms

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
