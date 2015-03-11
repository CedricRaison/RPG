from django import forms
from myapp.models import *
from django.contrib.auth.models import User


class UserForm(forms.Form):
	username = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=60)
	password = forms.CharField(max_length=30, min_length=4, widget=forms.PasswordInput)

class LoginForm(forms.Form):
	username = forms.CharField(max_length=60)
	password = forms.CharField(max_length=30, widget=forms.PasswordInput)

class NewPersonnageForm(forms.Form):
	nom = forms.CharField(max_length=30)
	vie = forms.IntegerField(max_value=10, min_value=0)
	force = forms.IntegerField(max_value=10, min_value=0)

class reponseForm(forms.Form):
	reponse = forms.CharField()
	