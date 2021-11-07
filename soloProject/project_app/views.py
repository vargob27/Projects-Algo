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
    sorted_tasks = Task.objects.all().order_by('due')
    context = {
        'user': this_user[0],
        'tasks': sorted_tasks,
        'assignedTasks': this_user[0].assigned_tasks.all(),
        'users': User.objects.all()
    }
    return render(request, 'home.html', context)

def completed(request):
    this_user = User.objects.filter(id=request.session['user_id'])
    sorted_tasks = Task.objects.all().order_by('due')
    context = {
        'user': this_user[0],
        'tasks': sorted_tasks,
        'assignedTasks': this_user[0].assigned_tasks.all(),
        'users': User.objects.all()
    }
    return render(request, 'completed.html', context)

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
    errors = Task.objects.task_validator(request.POST)
    if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/success')
    Task.objects.create(
        task_name = request.POST['task_name'],
        description = request.POST['description'],
        hours = request.POST['hours'],
        due = request.POST['due'],
        creator = User.objects.get(id=request.session['user_id'])
    )
    return redirect('/success')

def delete_task(request, task_id):
    to_delete = Task.objects.get(id=task_id)
    if request.session['user_id'] != to_delete.creator.id:
        messages.error(request, 'You are not the creator of the task you are trying to delete!')
        return redirect('/success')
    to_delete.delete()
    return redirect('/success')

def edit_task(request, task_id):
    context = {
        'task': Task.objects.get(id=task_id)
    }
    return render(request, 'editTask.html', context)

def update_task(request, task_id):
    errors = Task.objects.update_task_validator(request.POST)
    if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/task/update/{task_id}')
    to_update = Task.objects.get(id=task_id)
    to_update.task_name = request.POST['task_name']
    to_update.description = request.POST['description']
    to_update.hours = request.POST['hours']
    to_update.due = request.POST['due']
    to_update.save()
    return redirect('/success')

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('/success')

def task(request, task_id):
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'task': Task.objects.get(id=task_id),
        'loggedIn': request.session['user_id'],
        'users': User.objects.all()
    }
    return render(request, 'task.html', context)

def taskAssignment(request, task_id):
    context = {
        'users': User.objects.all(),
        'task': Task.objects.get(id=task_id)
    }
    return render(request, 'assignTask.html', context)

def assign_task(request, task_id):
    taskToAssign = Task.objects.get(id=task_id)
    userToAssign = User.objects.get(email=request.POST['email'])
    taskToAssign.assigned.add(userToAssign)

    return redirect('/success')

def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    context = {
        'user': User.objects.get(id=user_id),
        'loggedIn': User.objects.get(id=request.session['user_id']),
        'assignedTasks': user.assigned_tasks.all(),
        'userTickets': user.tickets.all(),
        'users': User.objects.all()
    }
    return render(request, 'profile.html', context)

def edit_profile(request, user_id):
    checkID = request.session['user_id']
    if checkID != user_id:
        return redirect('/success')
    context = {
        'user': User.objects.get(id=user_id),
        'loggedIn': request.session['user_id']
    }
    return render(request, 'editProfile.html', context)

def update_profile(request, user_id):
    errors = User.objects.update_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect(f'/user/edit/{user_id}')
    to_update = User.objects.get(id=user_id)
    to_update.first_name = request.POST['first_name']
    to_update.last_name = request.POST['last_name']
    to_update.email = request.POST['email']
    to_update.skill1 = request.POST['skill1']
    to_update.skill2 = request.POST['skill2']
    to_update.skill3 = request.POST['skill3']
    to_update.save()
    return redirect(f'/user/{user_id}')

def drop_task(request, task_id):
    loggedIN = request.session['user_id']
    task = Task.objects.get(id=task_id)
    task.assigned.remove(loggedIN)
    return redirect('/success')

def test(request):
    return render(request, 'test.html')