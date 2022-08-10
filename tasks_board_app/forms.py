from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Task


class TaskCreation(ModelForm):

    def __init__(self, user, **args, **kwargs):
        super(TaskCreation, self).__init__(*args,**kwargs)
        self.creator = user
        if user.is_superuser:
            self.fields['performer'].queryset = User.objects.all()
        else:
            self.fields['performer'].queryset = User.objects.filter(id=user.id)

        model = Task
        fields = ("text")
