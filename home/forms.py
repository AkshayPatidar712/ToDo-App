# from typing_extensions import Required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task
from django import forms


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['taskTitle', 'taskDesc']
        labels = {
            'taskTitle': 'Task Title',
            'taskDesc': 'Task Description'
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['taskDesc'].required = False


class usercreationform(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        labels = {
            'email': 'Email Address'

        }
