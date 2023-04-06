from django.urls import path 
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('Registro/', views.register, name="register"),
    path('Inicio/',views.homePage, name="homePage"),
    path('Perfil/',views.profile, name="profile"),
    path('EditarPerfil/',views.editProfile,name="editProfile"),
    
    
    path('home/', views.home, name="home"), 
    path('signup/', views.signup, name='signup'), 
    path('tasks/', views.tasks, name='tasks'), 
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin')
]