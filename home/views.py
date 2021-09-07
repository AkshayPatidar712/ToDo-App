from django.shortcuts import render

# Create your views here.
from django.shortcuts import redirect, render
from .forms import TaskForm
from .models import Task
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login_user(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list')
        else:
            return render(request, 'signup.html', {'form': form})


def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login_user')


def taskList(request):
    if request.user.is_authenticated:
        user = request.user
        form = Task.objects.filter(user=user)
        return render(request, 'list.html', {'form': form})


def taskAdd(request):

    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'task.html', {'form': form})
    else:
        if request.user.is_authenticated:
            user = request.user
            form = TaskForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = user
                todo.save()
            return redirect('list')
        else:
            return redirect('login_user')


def taskUpdate(request, id):
    if request.method == 'GET':
        # update = Task.objects.get(pk=id)
        form = TaskForm(instance=(Task.objects.get(pk=id)))
        return render(request, 'task.html', {'form': form})
    else:
        if request.user.is_authenticated:
            user = request.user
            # update = Task.objects.get(pk=id)
            form = TaskForm(request.POST, instance=(Task.objects.get(pk=id)))
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = user
                todo.save()
                return redirect('list')


def taskDelete(request, id):
    form = Task.objects.get(pk=id)
    form.delete()
    return redirect('list')
