from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
urlpatterns = [
	path('', views.home),
	path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html')),
	path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html')),
	path('register/', views.register, name='register')	
]