"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ecomerce.views import index
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from ecomerce.views import index, signup, UserViewSet
from item.serializer import CategorySerializer
from item.views import CategoryViewSet, ItemViewVset
from item.models import Category, Item

from ecomerce.views import UserViewSet
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         user = User
#         field = ('url', 'username', 'email', 'is_staff')
#
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'category',CategoryViewSet, basename=Category)
router.register(r'items', ItemViewVset, basename=Item)
urlpatterns = router.urls
urlpatterns = [
                  path('', include('ecomerce.urls')),
                  path('api/', include(router.urls)),
                  path('admin/', admin.site.urls),
                  path('item/', include('item.urls')),
                  path('dashboard/', include('dashboard.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

