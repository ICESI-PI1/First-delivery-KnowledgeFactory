from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
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
    
#Login view

def login(req):
    return render(req, 'test_app/login.html')

class LoginView(TemplateView): 
    template_name="test_app/login.html"

#Register view

def register(req):
    return render(req, 'test_app/Register.html')

class RegisterView(TemplateView):
    template_name="test_app/Register.html" 

#Home view

def homePage(req):
    projects=Project.objects.all()
    return render(req, 'test_app/MainPageEnterprise.html', {'projects':projects} )

class HomePageView(TemplateView):
    template_name="test_app/MainPageEnterprise.html" 

#Profile view

def profile(req):
    return render(req, 'test_app/Profile.html')

class ProfileView(TemplateView): 
    template_name="test_app/Profile.html"

#Edit profile view

def editProfile(req):
    return render(req, 'test_app/EditProfile.html')

class EditProfileView(TemplateView): 
    template_name="test_app/EditProfile.html"

#Information project view

def infoProject(req, id):
    project=get_object_or_404(Project,pk=id)
    return render(req, 'test_app/InfoProject.html', {'project':project})

class InfoProjectView(TemplateView):
    template_name="test_app/InfoProject.html"

    
#Request Appointment view

def requestAppointment(req):
    return render(req, 'test_app/RequestAppointment.html')

class RequestAppointmentView(TemplateView):
    template_name="test_app/RequestAppointment.html" 
    
#Request meeting view

def requestMeeting(req):
    return render(req, 'test_app/RequestMeeting.html')

class RequestMeetingView(TemplateView):
    template_name="test_app/RequestMeeting.html"

#Profile Meeting view

def profileMeeting(req):
    return render(req, 'test_app/ProfileMeeting.html')

class ProfileMeetingView(TemplateView):
    template_name="test_app/ProfileMeeting.html"

#Profile Favorites view

def profileFavorites(req):
    projects=Project.objects.all()
    return render(req, 'test_app/ProfileFavorites.html',{'projects':projects})

class ProfileFavoritesView(TemplateView):
    template_name="test_app/ProfileFavorites.html"


#Meeting Binnacle profile view

def meetingBinnacle(req):
    return render(req, 'test_app/MeetingBinnacleProfile.html')

class MeetingBinnacleView(TemplateView):
    template_name="test_app/MeetingBinnacleProfile.html"



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
