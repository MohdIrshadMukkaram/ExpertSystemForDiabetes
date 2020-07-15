from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.profile.first_name = form.cleaned_data.get('first_name')
			user.profile.last_name = form.cleaned_data.get('last_name')
			user.profile.email = form.cleaned_data.get('email')
			user.profile.age = form.cleaned_data.get('age')
			user.profile.gender = form.cleaned_data.get('gender')
			user.save()
			messages.success(request,f'Your account has been created! You can Log In now')
			return redirect('login')
	else:		
		form = UserRegisterForm()
	return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
	user = request.user
	age = Profile.objects.filter(user=user).values_list('age', flat=True)[0]
	return render(request,'users/profile.html',{'age':age})
