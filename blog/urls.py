from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='homePage'),
	path('aboutUs/', views.aboutUs,name='aboutUs'),
	path('contactUs/', views.contactUs,name='contactUs'),
	path('userLogin/', views.userLogin,name='userLogin'),
	path('userSignUp/', views.userSignUp,name='userSignUp'),
	path('userHome/', views.userHome,name='userHome'),



	
	
    
]