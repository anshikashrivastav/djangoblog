from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
	#inherit from models.Model
	user=models.OneToOneField(User,on_delete=models.CASCADE)#deletes profile if user deletes account
	image=models.ImageField(default='default.jpg',upload_to='profile_pics')#profile_pics is directory of profile pics uploaded
	#this can have multiple fields, for now only image used

	def __str__(self):
		return f'{self.user.username} Profile'

