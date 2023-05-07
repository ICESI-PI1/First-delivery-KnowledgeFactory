from django import forms

class loginForm(forms.Form): 
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control enter_input'}))
    password= forms.CharField(
        max_length=65, 
        widget=forms.PasswordInput(attrs={'class': 'form-control enter_input'}))
    

#class registerForm(forms.Form): 
 #   companyNit = forms.CharField(max_length=9, widget = forms.CharField(attrs={'class': 'form-control enter_input'}))
