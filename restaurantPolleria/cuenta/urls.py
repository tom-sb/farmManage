from django.urls import path
from . import views
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='cuenta/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='cuenta/logout.html'), name='logout'),
]
