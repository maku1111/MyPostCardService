# Views.py for Login.html by Maximilian Kuehn, 22/06/2023

# import from
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def loginaction(request):
    
    # read input fields after POST request
    if request.method=="POST":
        em_log=request.POST['email']
        pw_log=request.POST['password']
        
        # authentication and if successfull --> login
        user = authenticate(request, username=em_log, password=pw_log)

        if user is not None: 
            login(request, user)
            # redirect after successfull login
            return redirect('createpostcard')
        
        # if not successfull: error message
        else:
            messages.error(request,'Email or Password is wrong. Please log in again.')
            return redirect('login')
            
    return render(request,'Login.html')
