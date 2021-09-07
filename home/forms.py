# from typing_extensions import Required
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
