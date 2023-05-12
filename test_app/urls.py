from django.urls import path 
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name="login"),
    path('Registro/', views.RegisterView.as_view(), name="register"),
    path('Inicio/',views.homePage, name="homePage"),
    path('Perfil/',views.ProfileView.as_view(), name="profile"),
    path('Editar Perfil/',views.editProfile,name="editProfile"),
    path('Proyecto /<int:id>/',views.infoProject,name="productInformation"),
    path('Cotización de proyecto/',views.requestAppointment, name="requestAppointment"),
    path('Solicitar cita/',views.requestMeeting, name="requestMeeting"),
    path('Cotizaciones/',views.profileMeeting,name="profileMeeting"),
    path('Proyectos Favoritos/',views.profileFavorites, name="profileFavorites"),
    path('Bitácora de /',views.meetingBinnacle, name="meetingBinnacle"),
    
    
    path('TestDB/',views.testLitView.as_view(),name="testDB"),
    
    
    path('home/', views.home, name="home"), 
    path('signup/', views.signup, name='signup'), 
    path('tasks/', views.tasks, name='tasks'), 
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin')
]