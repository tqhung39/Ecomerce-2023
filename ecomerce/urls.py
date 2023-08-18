from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
app_name = 'ecomerce'

urlpatterns = [
    path('',views.index, name = 'index'),
    path('signup/',views.signup, name='signup' ),
    path('login/', auth_views.LoginView.as_view(template_name='ecomerce/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', views.logout_view, name='logout'),
]