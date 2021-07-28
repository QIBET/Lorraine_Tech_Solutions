from solutions.models import Sparepart
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout



# Create your views here.
def home(request):
    title = "Lorraine Tech Solutions"
    return render(request, 'index.html',{"title":title})

def register(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'registration/register.html', context)
def loginUser(request):
	if request.user.is_authenticated:
		return redirect('index')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username or password is incorrect')

		context = {}
		return render(request, 'registration/login.html', context)
def logoutUser(request):
	logout(request)
	return redirect('login')

def get_spares(request):
	parts = Sparepart.get_spareparts()
	return render(request, 'spares.html',{"parts":parts})
