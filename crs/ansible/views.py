from django.shortcuts import render
from ansible.models import *
# Create your views here.
def index(request):
	return render(request,'ansible/index.html',{})

def list_projects(request):
    projects = Project.objects.all()
    groups = []
    for project in projects:
        if project.group not in groups and project.group != None and project.group != '':
            groups.append(project.group)

    return render(request,"ansible/list_projects.html",{
        'projects': projects,
        'groups': groups,
        'request': request,
        })