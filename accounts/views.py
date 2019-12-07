
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout as dlogout
from django.contrib import messages

def sign_up(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']

		if User.objects.filter(username=username).exists():
			messages.info(request, 'Username already taken')
			return redirect('sign-up')
		elif User.objects.filter(email=email).exists():
			messages.info(request, 'Email already taken')
			return redirect('sign-up')
		else:
			user = User.objects.create_user(username=username, email=email, password=password)
			user.save()
			print('account created')
			return redirect('/')

	else:
		return render(request, 'sign-up.html')


	

def log_in(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, 'invalid credentials')
			return redirect('log-in')
	
	else:
		return render(request, 'log-in.html')

def log_out(request):

		auth.logout(request)
		return redirect('/')	