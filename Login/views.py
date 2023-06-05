from django.shortcuts import render,redirect
import mysql.connector as sql
em_log=''
pwd_log=''


# Create your views here.
def loginaction(request):
    global em_log,pwd_log
    
    if request.method=="POST":
        m_log=sql.connect(host="localhost",user="root",passwd="Maxikuehn13",database='mypostcardservice')
        cursor=m_log.cursor()
        d_log=request.POST
        for key,value in d_log.items():
            if key=="email":
                em_log=value
            if key=="password":
                pwd_log=value
        c="select * from users where email='{}' and password='{}'".format(em_log,pwd_log)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request, 'error.html')
        else: 
            return redirect('createpostcard')

    return render(request,'Login.html')
