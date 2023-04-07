from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

# Create your views here.

def login(req):
    return render(req, 'test_app/login.html')

def register(req):
    return render(req, 'test_app/Register.html')
    #if req.method == 'GET':
    #    return render(req, 'test_app/Register.html')
    #else:
    #    User.objects.create_user()
    
    #Deben intentar entrar a ese "create_user" y cambiar los datos o crear su propio formulario para hacer un register


def homePage(req):
    return render(req, 'test_app/MainPageEnterprise.html')

def profile(req):
    return render(req, 'test_app/Profile.html')

def editProfile(req):
    return render(req, 'test_app/EditProfile.html')


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
