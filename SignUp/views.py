from django.shortcuts import render,redirect
from django.contrib import messages
import mysql.connector as sql
fn=''
ln=''
em=''
pwd=''
pwd_conf=''



# Create your views here.
def signupaction(request):
    global fn,ln,em,pwd,pwd_conf

    if request.method=="POST":
        d=request.POST
        for key,value in d.items():
            if key=="password":
                pwd=value
            if key=="password2":
                pwd_conf=value
        
        if pwd==pwd_conf:
            print('PW sind gleich.')
            m=sql.connect(host="localhost",user="root",passwd="Maxikuehn13",database='mypostcardservice')
            cursor=m.cursor()

            for key,value in d.items():
                if key=="first_name":
                    fn=value
                if key=="last_name":
                    ln=value
                if key=="email":
                    em=value
                if key=="password":
                    pwd=value
                        
            c="insert into users Values('{}','{}','{}','{}')".format(fn,ln,em,pwd)
            cursor.execute(c)
            m.commit()
            return redirect('login')
            print('go to login.')
        
        else:
            messages.error(request, 'Passwords do not match!')
            print('Pw do not match.')
        
    return render(request,'Sign_up.html')