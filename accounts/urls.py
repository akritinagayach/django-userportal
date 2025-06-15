from django.shortcuts import redirect
from django.urls import path
from . import views


def home_redirect(request):
    return redirect('login')  # or 'signup' or 'dashboard'


urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('', home_redirect),
]



