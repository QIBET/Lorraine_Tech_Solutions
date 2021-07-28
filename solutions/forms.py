from .models import Phone,Laptop
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class PhoneForm(forms.ModelForm):
	
    class Meta:
        model = Phone
        exclude = ['user','date_posted']

class LaptopForm(forms.ModelForm):
	
    class Meta:
        model = Laptop
        exclude = ['user','date_posted']

