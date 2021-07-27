from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import CreateUserForm

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