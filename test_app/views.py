from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.views.generic.base import View, TemplateView
from test_app.models import Project, Company, User, Meeting, Role, Roles, Quotation, Binnacle
from .forms import loginForm, editCompanyForm, editProfileForm, crateMeetingBinacle, registerForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.db.models import Q



@require_GET
def get_available_admins(request):
    date = request.GET.get('date')
    time = request.GET.get('time')
    meetings = Meeting.objects.filter(date=date ,hour=time)
    busy_admin = [meeting.binnacle.admin.cc for meeting in meetings]

    admin_id = Role.objects.get(rolName='Admin')
    admin_role = Roles.objects.filter(role=admin_id.id)
    admin_role_id = [admin.user.cc for admin in admin_role]
    available_admins = User.objects.filter(
        Q(cc__in=admin_role_id) & ~Q(cc__in=busy_admin)
    )
    data = {
        'available_admins': [
            {'id': admin.cc, 'name': admin.fullname}
            for admin in available_admins
        ]
    }
    print(data)
    return JsonResponse(data)

def testLit(req):
    projects=Project.objects.all()
    if projects is None:
        print("vacio")
    else:
        print("aqui hay algo")
    return render(req, 'test_app/testLit.html', {'projects':projects})

class testLitView(TemplateView):
    template_name="test_app/testLit.html"
    
# Create your views here.
    
#Login view
class LoginView(TemplateView): 
    
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

#Register view

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
                                         phoneNumberU=req.POST['userPhone']
                                         )
        print("user: ", companyUser.__str__())

        company = Company.objects.create_company(nit=req.POST['companyNit'], 
                                                 name = req.POST['companyName'], 
                                                 phoneNumberC = req.POST['companyPhone'], 
                                                 address=req.POST['companyAddress'],
                                                 user = companyUser
                                                 )
        print("compania", company.__str__())
        companyUser.save()
        company.save()
        login(req, companyUser)
        message=''
        return redirect('homePage')

#Home view

class homePageView(TemplateView):
    template_name = "test_app/MainPageEnterprise.html"
    
    def get(self, req):
        projects = Project.objects.all()
        return render(req, 'test_app/MainPageEnterprise.html', {'projects':projects})

#Profile view    

class ProfileView(TemplateView): 
    template_name="test_app/Profile.html"
    
    def get (self, req):
        user=get_object_or_404(User,pk=req.user.cc)
        if Company.objects.filter(user=user.cc).count(): # Si el usuario tiene empresa asociada se hace get de la company 
            company=get_object_or_404(Company,user=req.user.cc)
        else:
            company=None
        return render(req, 'test_app/Profile.html', {'user':user,'company':company})

#Edit profile view
class EditProfileView(TemplateView): 
    template_name="test_app/EditProfile.html"
    
    def get(self, req):
        user=get_object_or_404(User,pk=req.user.cc)
        if Company.objects.filter(user=user.cc).count(): # Si el usuario tiene empresa asociada se hace get de la company y del form correspondiente
            company=get_object_or_404(Company,user=req.user.cc)
            formC=editCompanyForm(instance=company)
        else:
            company=None
            formC=None
        formU=editProfileForm(instance=user)
        return render(req, 'test_app/EditProfile.html', {'user':user,'company':company, 'formU':formU, 'formC':formC})
    
    def post(self, req):
        print(req.POST)
        user=get_object_or_404(User,pk=req.user.cc)
        formsU=editProfileForm(req.POST, instance=user)
        formsU.save()
        if Company.objects.filter(user=user.cc).count(): #Si el usuario esta asociado a una empresa se guarda el form de esa empresa
            company=get_object_or_404(Company,user=user.cc) 
            forms = editCompanyForm(req.POST, instance=company)
            forms.save()
        return redirect('profile')

#Information project view

class InfoProjectView(TemplateView):
    template_name="test_app/InfoProject.html"
    
    def get(self, req, id):
        project = get_object_or_404(Project,pk=id)
        return render(req, 'test_app/InfoProject.html', {'project': project})

    
#Request Appointment view

class RequestAppointmentView(TemplateView):
    template_name="test_app/RequestAppointment.html" 
    
#Request meeting view
class RequestMeetingView(TemplateView):
    template_name="test_app/RequestMeeting.html"
    
    def get(self, req, id):
        project = get_object_or_404(Project,pk=id)
        meetings=Meeting.objects.all()
        formM=crateMeetingBinacle()
        return render(req, 'test_app/RequestMeeting.html', {'meetings':meetings, 'formM':formM, 'project':project})
    
    def post(self, req, id):
        quotation = Quotation.objects.create(
            description='Pendiente de llenar',
            price=0
        )
        quotation.save()

        project = get_object_or_404(Project,pk=id)
        admin_id = req.POST.get('adminInput')
        admin= get_object_or_404(User,pk=admin_id)
        buy = get_object_or_404(Company,user=req.user.cc)

        binnacle = Binnacle.objects.create(
            project = project,
            buyer = buy,
            admin = admin,
            quotation = quotation
        )
        binnacle.save()

        date = req.POST.get('InputDate')
        time = req.POST.get('InputTime')
        summary = req.POST.get('FormControlTextarea1')
        meeting = Meeting.objects.create(
            state='Pendiente',
            date=date,
            hour=time,
            summary=summary,
            binnacle=binnacle
        )
        meeting.save()
        return redirect('projectInformation',id)
        


#Profile Meeting view

class ProfileMeetingView(TemplateView):
    template_name="test_app/ProfileMeeting.html"

    def get(self, req):
        user=req.user
        company=get_object_or_404(Company,user=user)
        binnacles=Binnacle.objects.filter(buyer=company)
        return render(req, 'test_app/ProfileMeeting.html',{'binnacles': binnacles, 'user':user})

#Profile Favorites view

class ProfileFavoritesView(TemplateView):
    template_name="test_app/ProfileFavorites.html"
    
    def get(self, req):
        projects = Project.objects.all()
        return render(req, 'test_app/ProfileFavorites.html',{'projects': projects})


#Meeting Binnacle profile view

class MeetingBinnacleView(TemplateView):
    template_name="test_app/MeetingBinnacleProfile.html"
    def get(self, req, id):
        binnacle = get_object_or_404(Binnacle, pk=id)
        meetings = Meeting.objects.filter(binnacle=id)
        return render(req, 'test_app/MeetingBinnacleProfile.html',{'binnacle': binnacle, 'meetings':meetings})


#Edit Meeting view

class EditMeetingView(TemplateView):
    template_name="test_app/EditMeeting.html"
    
    def get(self, req):
        #meeting = get_object_or_404(Meeting, pk=id)
        return render(req, 'test_app/EditMeeting.html')
    

# Add new meeting view

class AddNewMeetingView(TemplateView):
    template_name="test_app/AddNewMeeting.html"
    
    def get(self, req):
        #meeting = get_object_or_404(Meeting, pk=id)
        return render(req, 'test_app/AddNewMeeting.html')


# Edit quote view

class EditQuoteView(TemplateView):
    template_name="test_app/EditQuote.html"
    
    def get(self, req):
        #meeting = get_object_or_404(Meeting, pk=id)
        return render(req, 'test_app/EditQuote.html')



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
