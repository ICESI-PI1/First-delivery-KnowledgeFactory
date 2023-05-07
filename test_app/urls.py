from django.urls import path 
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name="signin"),
    path('Registro/', views.RegisterView.as_view(), name="register"),
    path('Inicio/',views.homePage, name="homePage"),
    path('Perfil/',views.ProfileView.as_view(), name="profile"),
    path('EditarPerfil/',views.EditProfileView.as_view(),name="editProfile"),
    path('Proyecto/<int:id>/',views.infoProject,name="productInformation"),
    path('TestDB/',views.testLitView.as_view(),name="testDB"),
    
    
    path('home/', views.home, name="home"), 
    path('signup/', views.signup, name='signup'), 
    path('tasks/', views.tasks, name='tasks'), 
    path('logout/', views.signout, name='logout'),
   # path('signin/', views.signin, name='signin')
]