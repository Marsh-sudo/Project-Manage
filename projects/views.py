from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Project,Task

# Create your views here.
def home(request):
    return render(request,"index.html")


def projectList(request):
    projects = Project.objects.all()
    context = {"projects":projects}
    return render(request,"projects/projects.html",context)


def projectDetail(request,pk):
   project = get_object_or_404(Project, id=pk)
   project_tasks = project.task_set.all()
   
   context = {'project':project,'project_tasks':project_tasks}
   return render(request, 'projects/project-detail.html',context)

def taskList(request):
    user_tasks = Task.objects.filter(assignee=request.user)
    tasks = Task.objects.filter(assignee=None)

    context = {'tasks':tasks,"user_tasks":user_tasks}
    return render(request,"projects/task.html",context)

def taskDetail(request,pk):
    task = get_object_or_404(Task,id=pk)
    context = {'task':task}
    return render(request,"projects/task-detail.html",context)