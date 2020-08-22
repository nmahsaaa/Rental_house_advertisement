from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='First Name', max_length = 100)
    last_name = forms.CharField(label='Last Name', max_length = 300)
    email = forms.EmailField(required = True)
    phone = forms.IntegerField(label='Phone No.', required= False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=300)
    email = forms.EmailField(required=True)
    phone = forms.IntegerField(label='Phone No.', required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']