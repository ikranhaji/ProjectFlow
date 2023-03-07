from django.forms import ModelForm
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ("name", "start_date", "due_date", "project", "assignee")
