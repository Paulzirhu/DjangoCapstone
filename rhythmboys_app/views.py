from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import BandMember, Album, Show, Merchandise
from django.contrib.auth import logout

def home(request):
    return render(request, 'rhythmboys_app/home.html')

def about(request):
    band_members = BandMember.objects.all()
    return render(request, 'rhythmboys_app/about.html', {'band_members': band_members})

def discography(request):
    albums = Album.objects.all()
    return render(request, 'rhythmboys_app/discography.html', {'albums': albums})

@login_required(login_url='login')
def book_tickets(request):
    return render(request, 'rhythmboys_app/book_tickets.html')

@login_required(login_url='login')
def purchase_merchandise(request):
    available_merchandise = Merchandise.objects.all()
    return render(request, 'rhythmboys_app/purchase_merchandise.html', {'available_merchandise': available_merchandise})
@login_required(login_url='login')
def choose_option(request):
    if request.user.is_authenticated:
        return render(request, 'rhythmboys_app/choose_option.html', {'username': request.user.username})
    else:
        messages.error(request, 'You need to log in to access this page.')
        return redirect('login')

def custom_login(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('choose_option')  # Redirect to choose-option page
        else:
            # Authentication failed, show error message
            error_message = "Invalid username or password. Please try again."
            return render(request, 'rhythmboys_app/login.html', {'error_message': error_message})
    else:
        return render(request, 'rhythmboys_app/login.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to choose_option page after successful registration
            return redirect('choose_option')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
