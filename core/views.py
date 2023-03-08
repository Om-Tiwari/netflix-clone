from django.shortcuts import render, redirect
from django.contrib import messages
from .views import *
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    context = {
        'title': "Netflix India - Watch TV Shows Online, Watch Movies Online"
    }
    return render(request, 'index.html', context)

def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Username Or Password is incorrect')
    context = {
        'title': "Netflix"
    }
    return render(request, 'signin.html', context)


def signout(request):
    logout(request)
    return redirect('core:signin')

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,f"Account Created Successfully for {user} ")
            return redirect('core:signin')
    context = {
        'form':form,
        'title': "Netflix"
    }
    return render(request, 'signup.html', context)