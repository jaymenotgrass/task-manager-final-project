from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Task
from .forms import RegisterUserForm, UserProfileForm, TaskForm





# Create your views here.
def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)  # Get tasks for the logged-in user
        total_tasks = tasks.count()
        pending_tasks = tasks.filter(completed=False)
        completed_tasks = tasks.filter(completed=True)

        # Pass the calculated variables to the template
        context = {
           'tasks': tasks,
           'total_tasks': total_tasks,
           'pending_tasks': pending_tasks,
           'completed_tasks': completed_tasks,
        }
    else:
        return render(request, 'index.html')
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user to the database
              # Log the user in after successful registration
            auth_login(request, user)
            return redirect('index')  # Redirect to the home page or any other page
    else:
        form = RegisterUserForm()

    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index')  # Redirect to the homepage or a dashboard
        else:
            # If the form is invalid, return the form with errors
            return render(request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def create_or_update_profile(request):

    # Try to get the profile if it exists, otherwise create it
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'create_or_update_profile.html', {'form': form})
@login_required
def task_list(request):
    user = request.user

    # Query for completed and pending tasks
    completed_tasks = Task.objects.filter(user=user, completed=True)
    pending_tasks = Task.objects.filter(user=user, completed=False)

    # Pass these to the template context
    context = {
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
    }

    return render(request, 'task_list.html', context)
@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'task_form.html', {'form': form})
@login_required
def task_edit(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_form.html', {'form': form})
@login_required
def task_delete(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'task_confirm_delete.html', {'task': task})
