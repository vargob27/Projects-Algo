from django.shortcuts import render, redirect
from django.contrib import messages, admin
from .models import *
import bcrypt

def index(request):
    return render(request, 'login.html')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0],
        'tasks': Task.objects.all()
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    # hash password
        hashed_pw = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
    # create User
        new_user = User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST[
                'last_name'], email=request.POST['email'], password=hashed_pw
        )
    # create session
        request.session['user_id'] = new_user.id
        return redirect('/success')
    return redirect('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/success')
    return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')

def create(request):
    Task.objects.create(
        task_name = request.POST['task_name'],
        description = request.POST['description'],
        hours = request.POST['hours'],
        due = request.POST['due'],
        creator = User.objects.get(id=request.session['user_id'])
    )
    return redirect('/success')