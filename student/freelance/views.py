from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! Please log in.')#save to database
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('freelance')  # Redirect to app page after login
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, "login.html", {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {'form': form})

def freelance(request):
    return render(request, 'home.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def profile(request):
    return render(request, 'profile.html')
def courses(request):
    return render(request, 'courses.html')
def skills(request):
    return render(request, 'skills.html')
def logout(request):
    return render(request, 'logout.html')
def dashboard_view(request):
    return render(request, 'dashboard.html')
    return redirect('home.html') 
def application_view(request):
    return render(request, 'application.html') 