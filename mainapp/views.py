from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login,logout



# Create your views here.
def runstatic(req):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(req, 'index.html',{'places':obj,'team':obj1})

def register(req):
    if req.method=='POST':
        username=req.POST.get('username')
        first_name=req.POST.get('first_name')
        last_name=req.POST.get('last_name')
        email=req.POST.get('email')
        password=req.POST.get('password')
        password2=req.POST.get('password2')
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(req,'Username taken')
                return render(req, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(req,'Email taken')
                return render(req, 'register.html')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                print('User created')
                messages.success(req,'Registration Successful, please login')
                return redirect('login')
        else:
            messages.info(req,'Password did not match')
    return render(req, 'register.html')

def login(req):
    if req.method=='POST':
        Username=req.POST.get('username')
        Password=req.POST.get('password')
        user=authenticate(username=Username,password=Password)
        if user is not None:
            auth_login(req,user)
            return redirect('/')
        else:
            messages.error(req,'Invalid Credentials, please try again!')
            return redirect('login')
    return render(req, 'login.html')


def user_logout(req):
    logout(req)
    return redirect('/')