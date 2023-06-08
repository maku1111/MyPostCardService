from django.shortcuts import render
import sqlite3
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required
# Create your views here.
def createpostcardaction(request):
    print('before post.')
    if request.method=="POST":
        print('start of post.')
        salutation = request.POST.get('salutation')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        postcard_message = request.POST.get('message')

        print('read recipient details.')

        # Daten in SQLite-Datenbank einfügen
        connection = sqlite3.connect('MyDatabase.db')
        cursor=connection.cursor()
        # Beispielabfrage ausführen
        cursor.execute("SELECT * FROM recipients")

        # Alle Zeilen aus der Abfrage abrufen
        rows = cursor.fetchall()

        # Ergebnis anzeigen
        for row in rows:
            print(row)

        # Verbindung schließen
        connection.close()
        #cursor = connection.cursor()
        #cursor.execute("INSERT INTO recipients (salutation, first_name, last_name, email, postcard_message) VALUES (?, ?, ?, ?, ?)",
        #             (salutation, first_name, last_name, email, postcard_message))
        #connection.commit()
        #connection.close()

        print('done.')

    return render(request,'Create_your_postcard.html')
