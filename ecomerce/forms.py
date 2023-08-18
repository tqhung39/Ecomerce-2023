from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from item.views import Item
from django.forms import ModelForm

class LoginForm(AuthenticationForm):
    # class Meta:
    #     model = User
    #     fields = ['username', 'password']
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password = forms.CharField(widget=forms.PasswordInput({
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput({
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput({
        'placeholder': 'Re-enter your password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

    # def clean(self):
    #     cleaned_data = super(SignUpForm, self).clean()
    #     password1 = cleaned_data.get("password")
    #     password2 = cleaned_data.get("confirm_password")
    #     if password1 != password2:
    #         self.add_error('confirm_password', "Password does not match")
    #     return cleaned_data


