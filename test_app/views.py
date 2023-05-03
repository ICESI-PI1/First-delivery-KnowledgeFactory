from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.views.generic.base import TemplateView
from test_app.models import Project
from test_app.models import Company

# Create your views here.

def testLit(req):
    projects=Project.objects.all()
    if projects is None:
        print("vacio")
    else:
        print("aqui hay algo")
    return render(req, 'test_app/testLit.html', {'projects':projects})

class testLitView(TemplateView):
    template_name="test_app/testLit.html"

def login(req):
    return render(req, 'test_app/login.html')

class LoginView(TemplateView): 
    template_name="test_app/login.html"



def register(req):
    return render(req, 'test_app/Register.html')

class RegisterView(TemplateView):
    template_name="test_app/Register.html" 


def homePage(req):
    projects=Project.objects.all()
    for proyecto in projects:
        print(proyecto.ownerCompany)
    return render(req, 'test_app/MainPageEnterprise.html', {'projects':projects} )

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
