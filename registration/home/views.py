from django.shortcuts import render

from django.contrib.auth.views import PasswordChangeView,PasswordResetView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

# Create your views here.


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful sign-up
    template_name = 'registration/signup.html'

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change_form.html'  # Specify your custom template
    success_url = reverse_lazy('password_change_done')  # Redirect to password change done page

class CustomPasswordResetView(PasswordResetView):
    template_name = 'password_reset_form.html'  # Specify your custom template
    success_url = reverse_lazy('password_reset_done')  # Redirect to password change done page

class ProfileView(TemplateView):
    template_name='registration/Profile.html'

def index(request):
    return render(request,'registration/index.html')

def dashboard(request):
    return render(request,'registration/dashboard.html')

# def profile(request):
#     return render(request,'registration/Profile.html')