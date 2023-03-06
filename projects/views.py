from django.shortcuts import render
from .models import Project


def list_projects(request):
    projects = Project.objects.all()
    context = {
        "project_list": projects
    }
    return render(request, "projects/list_projects.html", context)
