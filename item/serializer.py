from rest_framework import serializers
from .models import Category, Item
from django.contrib.auth.models import User

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Item
        fields = ('id', 'category', 'name', 'description', 'image', 'price', 'is_sold', 'created_at', 'created_by')
        lookup_field = 'category'


