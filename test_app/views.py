from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.views.generic.base import View, TemplateView
from test_app.models import Project
from test_app.models import Company
from .forms import loginForm

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
    return render(req, 'test_app/login.html') #Del anterior

class LoginView(View): #Hecho por Luis, usando singin.hml, diferencia con el que estaba q era un liginView simple que llamaba login.html
    
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


def homePage(req):
    projects=Project.objects.all()
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


def infoProject(req, id):
    project=get_object_or_404(Project,pk=id)
    return render(req, 'test_app/InfoProject.html', {'project':project})

class InfoProjectView(TemplateView):
    template_name="test_app/InfoProject.html"


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
