from django.shortcuts import render,redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings

import sqlite3
import os


@login_required
# Create your views here.
def createpostcardaction(request):
     
    if request.method=="POST":
        rec_salutation = request.POST.get('salutation')
        rec_first_name = request.POST.get('first_name')
        rec_last_name = request.POST.get('last_name')
        rec_email = request.POST.get('email')
        rec_postcard_message = request.POST.get('message')

        # Daten in SQLite-Datenbank einfügen
        connection = sqlite3.connect('MyDatabase.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO recipients (salutation, first_name, last_name, email, postcard_message) VALUES (?, ?, ?, ?, ?)",
                     (rec_salutation, rec_first_name, rec_last_name, rec_email, rec_postcard_message))
        connection.commit()
        connection.close()

        currentImageIndex=request.POST.get('myIndex')
        images = []
        for i in range(1, 31):
            images.append(f"design{i}.jpg")

        current_image = images[int(currentImageIndex)]
        #print(current_image)
         

        subject="You received an E-postcard"
        email=EmailMessage(subject,rec_postcard_message,settings.EMAIL_HOST_USER,[rec_email])
        email.attach_file('static/images/'+current_image)
        email.send()
        return redirect('logout')

    return render(request,'Create_your_postcard.html')
 