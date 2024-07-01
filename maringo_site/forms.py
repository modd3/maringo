from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput


from .models import Member 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput)
    password = forms.CharField(widget=PasswordInput)



class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'gender', 'next_of_kin', 'contact', 'age', 'status']

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter Your First Name'
            }),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Your Last Name'
            }),
            'gender': forms.TextInput(attrs={'placeholder': '(M/F)'
            }),
            'next_of_kin': forms.TextInput(attrs={'placeholder': 'Next of Kin'
            }),
            'name': forms.TextInput(attrs={'placeholder': 'Enter Your Name'
            }),
            'contact': forms.TextInput(attrs={'placeholder': 'Contact'
            }),
            'age': forms.TextInput(attrs={'placeholder': 'Age'
            }),
            'status': forms.TextInput(attrs={'placeholder': 'Marital Status'
            }),
        }

 