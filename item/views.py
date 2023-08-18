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

            return redirect('item:detail', pk=item.id)
    else:
        form = AddNewItemForm()
    return render(request, 'item/additem.html', {
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
        'title': 'Update Item Info'
    })
class CategoryViewSet(viewsets.ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer

class ItemViewVset(viewsets.ModelViewSet):
    queryset = Item.objects.all().select_related('category')
    serializer_class = ItemSerializer
    lookup_field = 'category'

# def OrderSummary(request,slug):
#     user = User.objects.all()
#     if user == request.user:
#         order = Order.objects.get_or_create(user=request.user, ordered=False)
#         return render(request, 'item/ordersummary.html', context={
#             'order': order,
#         })
#     else:
#         # messages.warning("You do not have an active order")
#         return redirect('ecomerce:index')

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
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                is_ordered=False,
            )[0]
            order.items.remove(order_item)
            order_item.delete()
    else:
        return redirect("item:detail", slug=slug)
    return redirect("item:detail", slug=slug)

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




