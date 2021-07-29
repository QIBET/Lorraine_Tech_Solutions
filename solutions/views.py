from solutions.models import Laptop, Phone, Sparepart
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CreateUserForm, LaptopForm, PhoneForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    title = "Lorraine Tech Solutions"
    return render(request, 'index.html',{"title":title})

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
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
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
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

@login_required (login_url="login")
def new_phone(request):
    current_user = request.user
    if request.method == 'POST':
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            phone = form.save(commit=False)
            phone.user = current_user

            phone.save()

        return redirect('home')

    else:
        form = PhoneForm()
    return render(request, 'new_phone.html', {"form": form})

@login_required (login_url="login")
def new_laptop(request):
    current_user = request.user
    if request.method == 'POST':
        form = LaptopForm(request.POST, request.FILES)
        if form.is_valid():
            laptop = form.save(commit=False)
            laptop.user = current_user

            laptop.save()

        return redirect('home')

    else:
        form = LaptopForm()
    return render(request, 'new_laptop.html', {"form": form})

def about(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def phone_repair(request):
	phone_repairs= Phone.get_phones()
	return render(request, 'phones.html',{"phone_repairs":phone_repairs})

def laptop_repair(request):
	laptop_repairs= Laptop.get_laptops()
	return render(request, 'laptops.html',{"laptop_repairs":laptop_repairs})