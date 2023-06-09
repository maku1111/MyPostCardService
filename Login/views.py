from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
import mysql.connector as sql

# Create your views here.
def loginaction(request):
    
    if request.method=="POST":
        em_log=request.POST['email']
        pw_log=request.POST['password']
        user = authenticate(request, username=em_log, password=pw_log)
        if user is not None: 
            login(request, user)
            return redirect('createpostcard')
        else:
            messages.error(request,'Email or Password is wrong. Please log in again.')
            return redirect('login')
            #implement something here
            #return render(request, 'error.html')

    return render(request,'Login.html')
