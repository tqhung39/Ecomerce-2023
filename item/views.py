from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, Category, OrderItem, Order
from django.db.models import Q
from .forms import AddNewItemForm, updateItemForm
from django.contrib.auth.decorators import login_required
from rest_framework import routers, serializers, viewsets, generics
from .serializer import CategorySerializer, ItemSerializer
from django.contrib import messages
from django.contrib.auth.admin import User
from django.utils import timezone
# Create your views here.

def searchItem(request):
    items = Item.objects.filter(is_sold=False)
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    category_id = request.GET.get('category',0)
    if category_id:
        items = items.filter(category_id=category_id)
    if query is not None:
        items = items.filter(Q(name__icontains=query)) | items.filter(Q(description__icontains=query))
    return render(request, 'item/search.html',{
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': category_id,
    })

def detail(request, slug):
    item = get_object_or_404(Item,slug=slug)
    return render(request, 'item/detail.html', {
        'item': item
    })

@login_required
def addNewItem(request):
    if request.method == 'POST':
        form = AddNewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user # Store user who create item
            item.save() # Create item
            return redirect('item:detail', slug=item.slug)
    else:
        form = AddNewItemForm()
    return render(request, 'item/add-item.html', {
        'form': form,
        'title': 'New Item',
    })

@login_required()
def deleteItem(request, slug):
    item = get_object_or_404(Item, slug=slug, created_by=request.user)
    item.delete()
    return render(request, 'ecomerce/index.html')

@login_required()
def updateItem(request, slug):
    item = get_object_or_404(Item, slug=slug, created_by=request.user)
    if request.method == 'POST':
        form = updateItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save() # save update data
            return redirect('item:detail',slug=item.slug)
    else:
        form = updateItemForm(instance=item)
    return render(request,'item/updateitem.html', {
        'form': form,
        'title': 'Update Item Info',
    })
class CategoryViewSet(viewsets.ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer

class ItemViewVset(viewsets.ModelViewSet):
    queryset = Item.objects.all().select_related('category')
    serializer_class = ItemSerializer
    lookup_field = 'category'


def Cart_Item_Count(request, user):
    if user.is_authenticated:
        order_qs = Order.objects.filter(user=user, ordered=False)
        if order_qs.exists():
            return order_qs[0].items.count()
    return render(request,'ecomerce/base.html',{
        'order': order_qs,
    })


def OrderSummary(request, slug):
    order = Order.objects.get(user=request.user)
    return render(request, 'item/ordersummary.html', {
        'order': order,
        })

@login_required()
def AddToCart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item = item,
        user = request.user,
        is_ordered=False,
    )
    order_queue = Order.objects.filter(user=request.user, ordered=False)
    if order_queue.exists():
        order = order_queue[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "The item in cart was updated")
            return redirect('item:order-summary', slug=slug)
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect('item:detail', slug=slug)

@login_required()
def RemoveFromCart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists(): #check if order is exist
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists(): #check if order item is exist or not
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                is_ordered=False,
            )[0]
            if order_item.quantity > 1 :
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
                messages.info(request, 'The item in cart was updated')
                # order_item.delete()
            return redirect('item:order-summary', slug=slug)
        else:
            return redirect("item:detail", slug=slug)
    else:
        return redirect("item:detail", slug=slug)







