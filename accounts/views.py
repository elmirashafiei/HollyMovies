from django.contrib.auth.views import LoginView , PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.
from .forms import MySignUpForm


class MyLoginView(LoginView):
    template_name = 'accounts/login.html'


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('movies')


class MySignUpView(CreateView):
  template_name = 'accounts/login.html'
  form_class = MySignUpForm
  success_url = reverse_lazy('accounts:login')