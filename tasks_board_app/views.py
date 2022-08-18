import imp
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.views.generic import CreateView, ListView, View, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from .models import Task
from .forms import TaskCreation
from django.contrib import messages



class Registration(CreateView):
    model = User
    template_name = 'form_page.html'
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
    template_name = 'form_page.html'
    success_url = '/'

    def get_form_kwargs(self):
        kwargs = super(TaskCreationPage, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.creator = self.request.user
        self.object.save()
        return super(TaskCreationPage, self).form_valid(form)
    
class StatusChangeView(LoginRequiredMixin, View):
    http_method_names= ['post']

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(id=request.POST['task_id'])
        if abs(int(request.POST['changer'])) != 1:
                messages.add_message(request, messages.INFO, 'You can only change the status by 1 point per time.')
        else:
            if request.user.is_superuser and task.status > 3:
                if task.status == 5 and int(request.POST['changer']) == 1:
                    messages.add_message(request, messages.INFO, 'Task alredy done.')
                else:
                    task.status += int(request.POST['changer'])
                    task.save()
                    


            elif task.performer == request.user:
                if int(request.POST['changer']) == 1:
                    if task.status > 3: 
                        messages.add_message(request, messages.INFO, 'Only Admin can do this.')
                    else:
                        task.status += int(request.POST['changer'])
                        task.save()                        
                if int(request.POST['changer']) == -1:
                    if task.status == 5:
                        messages.add_message(request, messages.INFO, 'Only Admin can do this.')
                    elif task.status == 1: 
                        messages.add_message(request, messages.INFO, 'Status does not exist.')
                    else:
                        task.status += int(request.POST['changer'])
                        task.save()

        return HttpResponseRedirect('/')


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    success_url= '/'
    template_name= 'form_page.html'

    def get_form_class(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        if self.request.user.is_superuser: 
            self.fields = ['text', 'performer']
        elif self.request.user == Task.objects.get(pk=pk).creator:
            self.fields = ['text']
        return super(UpdateTask, self).get_form_class()



class DeleteTask(LoginRequiredMixin, DeleteView):
    http_method_names= ['post']
    model= Task
    success_url= '/'

    def post(self, request, *args,**kwargs):
        if request.user.is_superuser:
            return super().post(request, *args, **kwargs)




