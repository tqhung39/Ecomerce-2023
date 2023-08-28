from django import forms
from .views import Item
class AddNewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'category',
            'name',
            'description',
            'image',
            'price',
            'slug',
        )
        widgets = {
            'category': forms.Select(attrs={
                'placeholder': 'Which category item belongs to',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Item Name',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'description': forms.TextInput(attrs={
                'placeholder': 'Item Description',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'image': forms.FileInput(attrs={
                'placeholder': 'Which category item belongs to',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Which category item belongs to',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'slug': forms.TextInput(attrs={
                'placeholder': 'Item Slug',
                'class': 'w-full py-4 px-6 rounded-xl'
            })
        }

class updateItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'name',
            'description',
            'image',
            'price',
            'slug'
        )
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Item Name',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'description': forms.TextInput(attrs={
                'placeholder': 'Item Description',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'image': forms.FileInput(attrs={
                'placeholder': 'Which category item belongs to',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'price': forms.NumberInput(attrs={
                'placeholder': 'Which category item belongs to',
                'class': 'w-full py-4 px-6 rounded-xl'
            }),
            'slug': forms.TextInput(attrs={
                'placeholder': 'Item Slug',
                'class': 'w-full py-4 px-6 rounded-xl'
            })
        }