from django.shortcuts import render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.


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
                return HttpResponse('User created succesfully')
            except:
                return render(req, 'test_app/signup.html',
                              {'form': UserCreationForm, "error": 'Passwords Do Not Match'})
        return render(req, 'test_app/signup.html',
                      {'form': UserCreationForm, "error": 'User Already Exists'})

