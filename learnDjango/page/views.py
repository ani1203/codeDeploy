from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'page/home.html')    # this method will render to home.html page


def signup(request):    # this method is created for creating the signup page
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():    # if form is valid it will be saved
            form.save()
            return redirect('home')    # this will redirect to the home.html page
    else:
        form = UserCreationForm()          # else again empty  form will be displayed
    return render(request, 'page/signup.html', {
        'form': form
    })
