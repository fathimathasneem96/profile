from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from myapp.forms import ProfileUpdateForm


# Create your views here.
def home(request):
    return render(request,'home.html')



@csrf_protect
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname= request.POST['fname']
        lname=request.POST['lname']
        email= request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name= fname
        myuser.last_name=lname

        myuser.save()

        return redirect('signin')

    return render(request, 'registration.html')

@csrf_protect
def signin(request):
    if request.method == "POST":
        username= request.POST['username']
        password1=request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            fname=user.first_name
            return redirect('profile')


        else:
            messages.error(request, "Invalid Credentials")
            return redirect('profile')

    return render(request, 'signin.html')
def signout(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            return redirect('profile')
    else:
        form = ProfileUpdateForm()
    return render(request, 'profile_update.html', {'form': form})

