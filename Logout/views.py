# Views.py for Login.html by Maximilian Kuehn, 22/06/2023

# import from
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# lock website without login
@login_required


def logoutaction(request):
    
    # call logout function if Logout button is clicked
    if request.method == 'POST':
        logout(request)
        # redirect to login after successfull logout
        return redirect('login')  
    else:
        return render(request, 'Logout.html')
    
