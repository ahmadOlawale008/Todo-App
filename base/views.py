from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound, HttpResponseForbidden
from base.forms import TaskForm
from base.models import Task, Category
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
import json

# from validate_email import validate_email
from django.core.validators import validate_email
# Create your views here
@login_required(login_url='basic_app:login')
def home(request):
    if request.method == 'GET':
        query = request.GET.get('query') if request.GET.get('query') != None else ''
        tasks = Task.objects.filter(user=request.user).order_by('time')
    return render(request, 'base/home.html', {'tasks': tasks})
@login_required(login_url='basic_app:login')
def editTask(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    form = TaskForm(instance=task)
    if request.user == task.user:
        if request.method == 'POST':
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                form.save(commit=False)
                task.save()
                return HttpResponseRedirect(reverse('basic_app:home'))
    else:
        return HttpResponseNotFound('Not found !!')    
    return render(request, 'base/edittask.html', {'form': form})
@login_required(login_url='basic_app:login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    if request.user == task.user:
        if request.method == 'POST':
            task.delete()
            return redirect('/')
    else:
        return HttpResponseNotFound('Not found !!')
    

@login_required(login_url='basic_app:login')
def addToTask(request):
    form = TaskForm
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return HttpResponseRedirect(reverse('basic_app:home'))
    return render(request, 'base/taskAdd.html', {'form': form})
def validate_useremail(request):
    if request.method == 'POST':
        data = json.loads(request.POST)
        email = email
        if not validate_email(email):
            return JsonResponse({'error': 'Invalid email'})
        if User.objects.filter(email=email).exists():
            return JsonResponse({'error': 'A user with this email already exists'}, status=400)
        else:
            return JsonResponse({'status': True})
def validate_username(request):
    if request.method == 'POST':
        data = json.loads(request)
        username = data['username']
    if not username.isalnum():
        return JsonResponse({'error': 'Ensure your username is alphanumeric'}, status=400)  

    if User.objects.filter(username=username).exists():
        return JsonResponse({'error': 'A uesr with this username already exist'}, status=400)  
    else:
        return JsonResponse({'status': True})  
def validate_password(request):
    if request.method == 'POST':
        data = json.loads(request)
        password = data['password']  
        if len(str(password)) < 7:
            return  JsonResponse({'error': 'Minimum length of password is 7 due to security reasons'}, status=400)
        else:
            return JsonResponse({'status': True})
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        if not validate_email(email):
            return redirect('basic_app:login')
        
        if password != confirmPassword:
            print('user-eq error')
            
            return redirect('basic_app:login')
        if len(str(password).strip()) < 7:
            print('pass-strip error')
            
            return redirect('basic_app:login')
        if User.objects.filter(username=username) == False:
            print('user-us error')
            return redirect('basic_app:login')
        if User.objects.filter(email=email).exists():
            print('user-ex error')
            return redirect('basic_app:login')
        if len(str(username).strip()) < 1:
            print('username-str error')
            
            return reverse('basic_app:login')
        if not username.isalnum():
            print('user-aln error')
            return reverse('basic_app:login')
        else:
            user = User.objects.create_user(username=username, email=email)
            user.save()
            user.set_password(confirmPassword)
            user.save()
            return HttpResponseRedirect(reverse('basic_app:login'))
    return render(request, 'base/register.html')

def user_login(request):
    if request.method  == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('basic_app:home'))
    return render(request, 'base/signin.html')


def user_logout(request):
    logout(request)
    return redirect('/')

def addCategory(request, task_pk):
    task = get_object_or_404(Task, id=task_pk)
    if request.method == 'post':
        choice = request.POST.get('choice')
        category = Category.objects.create()
        category.choices.append()
    