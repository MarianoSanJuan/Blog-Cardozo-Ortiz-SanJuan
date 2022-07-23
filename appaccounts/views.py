from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
# from accounts.models import MasDatosUsuario
from .forms import MyUserCreationForm

# Create your views here.

def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request, user)
                return redirect('inicio')
            else:
                return render(request, 'accounts/login.html', {'form': form})
        else:
            return render(request, 'accounts/login.html', {'form': form})
        
    
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def registro(request):
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    
    form = MyUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})