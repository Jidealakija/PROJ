from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


@login_required
def homepage (request):
    return render(request, 'backend/home.html')

def register (request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(username=name).exists():
                messages.info(request, 'Sorry that username is taken')
                return redirect ('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is taken already')
                return redirect ('register')
            else:
                new_user = User.objects.create_user(username=name, email=email)
                new_user.set_password(password)
                new_user.save()
                messages.success(request, 'Thank you for signing up!!')
                return redirect ('/')
        else:
            messages.error(request, 'Both passwords must match')
            return redirect('register')
    return render(request, 'backend/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect ('/')
        else:
            messages.error(request, 'Oops, something went wrong!')
            return redirect ('login')
    return render(request, 'backend/login.html')

def logout (request):
    auth.logout(request)
    return redirect('/')
