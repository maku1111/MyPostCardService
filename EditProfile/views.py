# Views.py for EditProfile.html by Maximilian Kuehn, 22/06/2023

# import from
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# lock website without login
@login_required
def editprofileaction(request):
    if request.method == 'POST':

        # ask which button was clicked, read out data afterwards
        if 'save_changes' in request.POST:
            new_email = request.POST.get('new_email')
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            
            # if password and confirmed password match and are not empty, update user in database
            if new_password and confirm_password and new_password == confirm_password:
                user = request.user
                user.set_password(new_password)
                user.save()
            
            # if email input field not empty, update email and username (same) of user in database
            if new_email:
                print('email ausgefüllt')
                user = request.user
                user.username = new_email
                user.email = new_email
                user.save()

                return redirect('logout')

        # delete user, if "delete"-button was clicked
        elif 'delete_profile' in request.POST:
            user = request.user
            user.delete()
            return redirect('signup')

    return render(request, 'EditProfile.html')
