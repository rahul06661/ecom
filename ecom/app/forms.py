from django import forms

from django.contrib.auth.forms import  UserCreationForm , AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import widgets


class CustomerRegistrationForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm_Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email=forms.CharField(label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        widgets={'username':forms.TextInput(attrs={'class':'form-control'})}
        fields=['username','email','password1','password2']

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    



