from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()#by default it takes required, can make required=False


	class Meta:
		model=User
		fields=['username','email','password1','password2']
		#class meta gives nested space for configurations
		#so we now use UserRegistrationForm instead of UserCreationForm so we now need to replace the names


class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()#by default it takes required, can make required=False


	class Meta:
		model=User
		fields=['username','email']
#inheriting


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['image']
#need to add above created forms to views.py 