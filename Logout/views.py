from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.
def logoutaction(request):
    
    if request.method == 'POST':
        logout(request)
        return redirect('login')  # Geben Sie den Namen Ihrer Login-Seite an
    else:
        return render(request, 'Logout.html')
    
