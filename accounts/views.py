from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as django_logout


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    error = None  # initialize error message
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error = 'Invalid username or password'  # set error message
    return render(request, 'accounts/login.html', {'error': error})


@login_required
def dashboard_view(request):
    if request.user.user_type == 'Doctor':
        return render(
            request, 'accounts/doctor_dashboard.html', {'user': request.user}
        )
    else:
        return render(
            request, 'accounts/patient_dashboard.html', {'user': request.user}
        )


def logout_view(request):
    django_logout(request)
    return redirect('login')