from django.shortcuts import render
from item.models import Category, Item
from django.forms import Form
from ecomerce.forms import SignUpForm, LoginForm
from django.contrib.auth import logout
from ecomerce.serializer import UserSerializer
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User

# Create your views here.
from django.http import HttpResponse
def index(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'ecomerce/index.html', {
        'items': items,
        'categories': categories,
    })
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return ('/')
    else:
        form = SignUpForm()
    return render(request, 'ecomerce/signup.html',{
        'form': form
    })

def logout_view(request):
    item = Item.objects.all()
    categories = Category.objects.all()
    logout(request)
    return render(request, 'ecomerce/index.html', {
        'items': item,
        'categories': categories,
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer