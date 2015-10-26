from django.shortcuts import render
from ansible.models import *
from django.http import HttpResponseRedirect,HttpResponse
from django.core import urlresolvers

from storefile import ensure_project_dir

from guardian.shortcuts import assign_perm,remove_perm,get_perms,get_users_with_perms

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

def add_project(request):
    page_errors=None

    if request.method == 'POST':
        name = request.POST.get("name")
        desc = request.POST.get("description")
        scmtype = request.POST.get("scmtype")
        scmurl = request.POST.get("scmurl")
        group = request.POST.get("group")

        # check name
        name_re = re.match("\w+",name)
        proj = Project.objects.filter(name = name)
        # need a message
        if proj or not name:
            raise Exception("project name required!")

        try:
            project=Project(name=name)
            project.description=desc
            project.created_by=request.user
            project.scmtype = scmtype
            project.scmurl = scmurl
            project.group = group
            project.save()

            dir_result = ensure_project_dir(project.name)
            user = request.user
            perms = has_perms(user,project)
            if perms == []:
                assign_perm('access_proj',user,project)
                assign_perm('config_proj',user,project)
                assign_perm('execute_proj',user,project)
                assign_perm('manage_proj',user,project)

        except Exception,e:
            print e
            raise Exception()
        return HttpResponseRedirect(urlresolvers.reverse('list_projects'))


    return render("ansible/add_project.html",request,{
        'action': urlresolvers.reverse('add_project'),
        'page_errors':page_errors,
        'request': request,
        })