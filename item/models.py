from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.urls import reverse
from rest_framework import routers, serializers, viewsets
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    price = models.FloatField(blank=True)
    is_sold = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name

    def get_object_or_404(self, pk):
        pass

    def get_absolute_url(self):
        return reverse("item:detail", kwargs={
            'slug': self.slug,
        })

    def get_add_to_cart_url(self):
        return reverse("item:add-to-cart", kwargs={
            'slug': self.slug,
        })

    def get_remove_from_cart_url(self):
        return reverse('item:remove-from-cart', kwargs={
            'slug': self.slug,
        })

    def get_order_summary_url(self):
        return reverse('item:order-summary', kwargs={
            'slug': self.slug,
        })
class OrderItem(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='order_item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    is_ordered = models.BooleanField(default=False)

    class Meta:
        ordering = ('item',)
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return f"{self.quantity} of {self.item}"

    def get_object_or_404(self, slug):
        pass

    def get_total_item_price(self):
        return self.quantity * self.item.price

class Order(models.Model):
    user = models.ForeignKey(User, related_name='ordered_user', on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def total_price(self):
        total_price = 0
        for order_item in self.items.all():
            total_price += order_item.get_total_item_price()
        return total_price

    # def get_order_summary_url(self):
    #     return reverse('item:order-summary', kwargs={
    #         'user': self.user
    #     })

    # def get_total_item_in_cart(self):
    #     return self.ordered

