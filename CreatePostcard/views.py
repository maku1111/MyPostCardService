# Views.py for Create_your_postcard.html by Maximilian Kuehn, 22/06/2023

# import from
from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings

# imports
import sqlite3
import os

# lock website without login 
@login_required
def createpostcardaction(request):
     
    if request.method=="POST":

        # reading data from imput fields after POST request
        rec_salutation = request.POST.get('salutation')
        rec_first_name = request.POST.get('first_name')
        rec_last_name = request.POST.get('last_name')
        rec_email = request.POST.get('email')
        rec_postcard_message = request.POST.get('message')

        # write data to sqlite3 database, close connection after that
        connection = sqlite3.connect('MyDatabase.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO recipients (salutation, first_name, last_name, email) VALUES (?, ?, ?, ?)",
                     (rec_salutation, rec_first_name, rec_last_name, rec_email))
        connection.commit()
        connection.close()

        # get current postcard motive, which will be sent by postcard service
        currentImageIndex=request.POST.get('myIndex')

        # fill array images with file names of images
        images = []
        for i in range(1, 31):
            images.append(f"design{i}.jpg")

        # get current image from array with helf of currentImageIndex
        current_image = images[int(currentImageIndex)]
                 
        # Create data for Email and attach image
        subject="You received an E-postcard"
        email=EmailMessage(subject,rec_postcard_message,settings.EMAIL_HOST_USER,[rec_email])
        email.attach_file('static/images/'+ current_image)
        email.send()
        return redirect('logout')

    return render(request,'Create_your_postcard.html')
 