from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
import os
def sign_in(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            login(request, user)
            return redirect('http://127.0.0.1:8000/home')
        else:
            return render(request, 'Wrong_Credentials.html')

    return render(request, 'signin.html')

# def sign_up(request):
#
#     if request.method == 'POST':
#         username = request.POST['username']
#         fname = request.POST['fname']
#         lname = request.POST['lname']
#         email = request.POST['email']
#
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         myuser = User.objects.create_user(username, password1)
#         User.first_name = fname
#         User.last_name = lname
#         myuser.set_password(password1)
#         myuser.save()
#         messages.success(request, "Your account has been created successfully!")
#         return redirect('signin')
#     return render(request, 'signup.html', {})

def sign_up(request):

    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']

        password1 = request.POST['password1']
        password2 = request.POST['password2']
        myuser = User.objects.create_user(username, password1)
        User.first_name = fname
        User.last_name = lname
        myuser.set_password(password1)
        myuser.save()
        messages.success(request, "Your account has been created successfully!")
        return redirect('signin')
    return render(request, 'signup.html', {})


def sign_out(request):
    return render(request, 'signout.html')
