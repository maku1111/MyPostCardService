from django.shortcuts import render
import sqlite3
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage, get_connection, send_mail
from django.conf import settings



@login_required
# Create your views here.
def createpostcardaction(request):
    print('before post.')
    if request.method=="POST":
        print('start of post.')
        rec_salutation = request.POST.get('salutation')
        rec_first_name = request.POST.get('first_name')
        rec_last_name = request.POST.get('last_name')
        rec_email = request.POST.get('email')
        rec_postcard_message = request.POST.get('message')

        print('read recipient details.')

        # Daten in SQLite-Datenbank einfügen
        connection = sqlite3.connect('MyDatabase.db')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO recipients (salutation, first_name, last_name, email, postcard_message) VALUES (?, ?, ?, ?, ?)",
                     (rec_salutation, rec_first_name, rec_last_name, rec_email, rec_postcard_message))
        connection.commit()
        connection.close()

        print('done writing to database.')
        print('send email')


        subject="You received an E-postcard"
    
     
        send_mail(subject,rec_postcard_message,settings.EMAIL_HOST_USER,[rec_email])

        #with get_connection(  
         #   host=settings.EMAIL_HOST, 
          #  port=settings.EMAIL_PORT,  
           # username=settings.EMAIL_HOST_USER, 
            #password=settings.EMAIL_HOST_PASSWORD, 
            #use_tls=settings.EMAIL_USE_TLS
        #) as connection:  
         #   subject = 'You received an E-Postcard' 
          #  email_from = settings.EMAIL_HOST_USER  
           # recipient_list = email  
            #message = postcard_message 
            #EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()


    return render(request,'Create_your_postcard.html')
 