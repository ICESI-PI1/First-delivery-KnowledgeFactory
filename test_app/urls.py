from django.urls import path 
from . import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LoginView.as_view(), name="signin"),
    path('Registro/', views.RegisterView.as_view(), name="register"),
    path('Inicio/',views.homePageView.as_view(), name="homePage"),
    path('Perfil/',views.ProfileView.as_view(), name="profile"),
    path('EditarPerfil/',views.EditProfileView.as_view(), name="editProfile"),
    path('Proyecto$<int:id>/',views.InfoProjectView.as_view(), name="projectInformation"),
    path('Cotización$de$proyecto/',views.RequestAppointmentView.as_view(), name="requestAppointment"),
    path('Solicitar$cita$<int:id>/', views.RequestMeetingView.as_view(), name="requestMeeting"),
    path('Cotizaciones/',views.ProfileMeetingView.as_view(), name="profileMeeting"),
    path('Proyectos$Favoritos/',views.ProfileFavoritesView.as_view(), name="profileFavorites"),
    path('Bitácora$de$<int:id>/',views.MeetingBinnacleView.as_view(), name="meetingBinnacle"),
    path('Editar$cita/',views.EditMeetingView.as_view(), name="editMeeting"),
    path('Añadir$nueva$cita/',views.AddNewMeetingView.as_view(), name="addNewMeeting"),
    path('Editar$cotización/',views.EditQuoteView.as_view(), name="editQuote"),
    
    
    path('TestDB/',views.testLitView.as_view(),name="testDB"),
    path('get_available_admins/', views.get_available_admins, name='get_available_admins'),
    
    path('home/', views.home, name="home"), 
    path('signup/', views.signup, name='signup'), 
    path('tasks/', views.tasks, name='tasks'), 
    path('logout/', views.signout, name='logout'),
]