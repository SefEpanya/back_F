from django.shortcuts import render, redirect
from .forms import UserForm

#import mysql.connector as sql
#fn =''
#em=''
#pwd=''
# Views for fifi app


def fileFinder(request):
    """
    Handle files uploads
    Args:
        request (POST): New file upload
    """
    return render(request, "index.html")


def registration(request):
#    global fn,em,pwd
#    if request.method =='POST':
#        m=sql.connect(host="localhost",user="root",password="",database="dbfifi")
#        cursor=m.cursor()
#        d=request.POST
#        for key,value in d.items():
#            if key=="full_name":
#                fn=value
#            if key=="email":
#                em=value
#            if key=="password":
#                pwd=value
#    c="insert into users('{}','{}','{}')".format(fn,em,pwd)
#    cursor.execute()
#    m.commit()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userpage')
    else:
        form = UserForm()
    return render(request, "register-page.html", {'form': form })


def upload(request):
    return render(request, "landing-page.html")


def userPage(request):
    return render(request, "profile-page.html")
    