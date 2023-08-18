from django.urls import path, include
from item.views import detail
from . import views
from . forms import AddNewItemForm, updateItemForm
from .serializer import CategorySerializer
from rest_framework import routers, viewsets
app_name = 'item'


urlpatterns = [
    path('<slug>/', views.detail, name='detail'),
    path('add-item/', views.addNewItem, name='add-item'),
    path('<slug>/update-item/', views.updateItem, name='update-item'),
    path('<slug>/delete/', views.deleteItem, name='delete-item'),
    path('search/', views.searchItem, name='search-item'),
    path('add-to-cart/<slug>',views.AddToCart, name='add-to-cart'),
    path('remove-from-cart/<slug>',views.RemoveFromCart, name='remove-from-cart'),
    # path('<slug>/order-summary/', views.OrderSummary, name='order-summary' )
    # path('category-list/', include('rest_framework.urls', namespace='rest_framework')),
]