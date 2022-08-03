from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    return render(request,"login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['Username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['Email']
        password = request.POST['Password']
        cpword = request.POST['confirm password']
        if password == cpword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken taken")
                return redirect('register')
            user = User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname, email=email)
            user.save()
            print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")