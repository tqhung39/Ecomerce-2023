from django.urls import path
from . import views
from dashboard.views import index

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='dashboard')
]