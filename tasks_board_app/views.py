import imp
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskCreation


class Registration(CreateView):
    model = User
    template_name = 'login.html'
    form_class = UserCreationForm
    success_url = '/'


class Login(LoginView):
    template_name = 'login.html'


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'

class BoardPage(LoginRequiredMixin, ListView):
    queryset = Task.objects.all()
    template_name = 'board.html'
    allow_empty= True


class TaskCreationPage(LoginRequiredMixin, CreateView):
    form_class = TaskCreation
    model = Task
    template_name = 'login.html'
    success_url = '/'