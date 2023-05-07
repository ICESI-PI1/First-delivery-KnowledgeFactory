from django.urls import path 
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name="signin"),
    path('Registro/', views.RegisterView.as_view(), name="register"),
    path('Inicio/',views.HomePageView.as_view(), name="homePage"),
    path('Perfil/',views.ProfileView.as_view(), name="profile"),
    path('EditarPerfil/',views.EditProfileView.as_view(),name="editProfile"),
    
    
    path('home/', views.home, name="home"), 
    path('signup/', views.signup, name='signup'), 
    path('tasks/', views.tasks, name='tasks'), 
    path('logout/', views.signout, name='logout'),
   # path('signin/', views.signin, name='signin')
]