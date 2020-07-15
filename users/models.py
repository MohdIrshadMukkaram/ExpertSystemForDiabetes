
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female'),
)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	email = models.EmailField()
	first_name = models.CharField(max_length=100, blank=True)
	last_name = models.CharField(max_length=100, blank=True)
	age = models.IntegerField(default=20)
	gender= models.CharField(max_length=2,choices=GENDER_CHOICES)
	image = models.ImageField(default='default.jpg', upload_to='profile_pics')

	def __str__(self):
		return f'{self.user.username} Profile'

	 