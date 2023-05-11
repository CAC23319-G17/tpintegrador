from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm
from .forms import LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required


def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado con Exito !!!')
			return redirect('index')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'userApp/register.html', context)

# def login(request):
# 	if request.method == 'POST':
# 		form = LoginForm(request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data['username']
# 			password = form.changed_data['password']
# 			user = authenticate(username=username, password=password)

def profile(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
	else:
		user = current_user
	return render(request, 'userApp/profile.html', {'user':user})