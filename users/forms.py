from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)
class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))
	last_name = forms.CharField(max_length=32)
	age = forms.DecimalField(min_value=20,max_value=80, help_text='Greater than 20')
	gender= forms.CharField(label='Gender', widget=forms.Select(choices=GENDER_CHOICES))

	class Meta:
		model = User
		fields = ['first_name','last_name','age','gender','username','email','password1','password2']
	