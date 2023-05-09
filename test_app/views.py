from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.views.generic.base import View, TemplateView
from .forms import loginForm, registerForm
from .models import *

# Create your views here.


class LoginView(View): 
    
    template_name="test_app/signin.html"
    form_class = loginForm
    
    def get(self, req):
        form=self.form_class()
        message=''
        return render(req, self.template_name, context={'form': form, 'message': message})

    #href="{% url 'signin' %}"
    def post(self, req): 
        print(req.POST)
        form = self.form_class(req.POST)
        user=authenticate(req, username=req.POST['email'], 
                          password=req.POST['password'])
        if user is None: 
            message = 'Login failed!'
            return render(req, self.template_name, context={'form': form, 'message': message})
        else: 
            login(req, user)
            return redirect('homePage')


    


def register(req):
    return render(req, 'test_app/Register.html')

class RegisterView(TemplateView):
    template_name="test_app/Register.html" 
    form_class = registerForm

    def get(self, req):
        form=self.form_class(req.POST)
        message=''
        return render(req, self.template_name, context={'form': form, 'message': message})

    def post(self, req): 
        print(req.POST)
        form=self.form_class(req.POST)
        
        companyUser =  User.objects.create_user(email=req.POST['userEmail'],
                                         password=req.POST['userPassword'], 
                                         fullname=req.POST['userName'], 
                                         cc=req.POST['userCC'], 
                                         birthday=req.POST['userBirthday'], 
                                         phoneNumber=req.POST['userPhone']
                                         )
        print("user: ", companyUser.__str__())

        company = Company.objects.create_company(nit=req.POST['companyNit'], 
                                                 name = req.POST['companyName'], 
                                                 phoneNumber = req.POST['companyPhone'], 
                                                 address=req.POST['companyAddress'],
                                                 user = companyUser
                                                 )
        print("compania", company.__str__())
        companyUser.save()
        company.save()
        login(req, companyUser)
        message=''
        return redirect('homePage')


def homePage(req):
    return render(req, 'test_app/MainPageEnterprise.html')

class HomePageView(TemplateView):
    template_name="test_app/MainPageEnterprise.html" 



def profile(req):
    return render(req, 'test_app/Profile.html')

class ProfileView(TemplateView): 
    template_name="test_app/Profile.html"


def editProfile(req):
    return render(req, 'test_app/EditProfile.html')

class EditProfileView(TemplateView): 
    template_name="test_app/EditProfile.html"



#Vistas por defecto de Django

def home(req):
    return render(req, 'test_app/home.html')


def signup(req):

    if req.method == 'GET':
        return render(req, 'test_app/signup.html', {'form': UserCreationForm})
    else:
        print("procesando datos", req.POST)
        if req.POST['password1'] == req.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(
                    username=req.POST['username'], password=req.POST['password1'])
                user.save()
                login(req, user)
                print("usuario guardado")
                return redirect('tasks')
                #return HttpResponse('User created succesfully')
            except IntegrityError:
                return render(req, 'test_app/signup.html', {'form': UserCreationForm, "error": 'User Already Exists'})
        return render(req, 'test_app/signup.html',
                      {'form': UserCreationForm, "error": 'Passwords do not match'})



def tasks(req): 
    return render(req, 'test_app/tasks.html')

def signout(req): 
    logout(req)
    return redirect('home')

def signin(req): 
    if req.method == "GET":
        return render(req, 'test_app/signin.html', {'form': AuthenticationForm})
    else:
        user=authenticate(req, username=req.POST['username'], password=req.POST['password'])
        if user is None: 
            return render(req, 'test_app/signin.html', {'form': AuthenticationForm, 'error': 'User Does Not Exists'})
        else: 
            login(req, user)
            print("ingreso exitoso")
            return redirect('tasks')
