from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .views import *
from .forms import SignUpForm
# Create your views here.


def index(request):
    context = {
        'title': "Netflix India - Watch TV Shows Online, Watch Movies Online"
    }
    return render(request, 'index.html', context)


def login(request):

    context = {
        'title': "Netflix"
    }
    return render(request, 'login.html', context)


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'title': "Netflix"
    }
    return render(request, 'signup.html', context)
