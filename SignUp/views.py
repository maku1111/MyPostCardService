from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def signupaction(request):

    if request.method=="POST":
        fn=request.POST.get('first_name')
        ln=request.POST.get('last_name')
        em=request.POST.get('email')
        pw=request.POST.get('password')
        pw_conf=request.POST.get('password_conf')


        if pw!=pw_conf:
            messages.error(request, 'Passwords do not match!')
            print('Pw do not match.')

        else:
            my_user = User.objects.create_user(username=em, email=em, password=pw)
            my_user.first_name = fn
            my_user.last_name = ln
            my_user.save()
            return redirect('login')    
        
    return render(request,'Sign_up.html')