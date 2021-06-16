from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm, AnnonceForm

# Create your views here.
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('profile')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')
			else:
				messages.error(request, 'Veuillez rééssayer')
				return redirect('register')
		context = {'form':form}
		return render(request, 'register/signup.html', context)

def loginPage(request):
	nextURL = request.POST.get("next", None)
	if request.user.is_authenticated:
		return redirect('profile')
	else:
		if request.method == 'POST':
			Login = request.POST.get('login')
			passwd =request.POST.get('passwd')
			user = authenticate(request, username=Login, password=passwd)
			if user is not None:
				if nextURL in request.POST:
					login(request, user)
					return redirect('postAnnonce')
				else:
					login(request, user)
					return redirect('profile')
			else:
				messages.info(request, 'Username OR password is incorrect')
		context = {}
		return render(request, 'login/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')

def home(request):
	form = Ajout.objects.all()
	return render(request, 'home/home.html', {'form':form})

@login_required(login_url='login')
def profile(request):
	return render(request, 'profile/profile.html')

@login_required(login_url='login')
def postAnnonce(request):
	if request.method == 'POST':
		form = AnnonceForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, 'Annoce crée avec succés')
		else:
			messages.error(request, 'Problème')
	else:
		form = AnnonceForm()
	return render(request, 'postAnnonce/postAnnonce.html', {'form':form})

def autre(request):
	return render(request, 'autre/autre.html')

def modelisme(request):
	return render(request, 'modelisme/modelisme.html')

def oenologie(request):
	return render(request, 'oenologie/oenologie.html')

def philatelie(request):
	return render(request, 'philatelie/philatelie.html')

@login_required(login_url='login')
def post_edit(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = CreateUserForm()
    return render(request, 'test/test.html', {'form': form})

def modifCompt(request):
	return render(request, 'modif/modifCompt.html')