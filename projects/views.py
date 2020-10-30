from django.shortcuts import render
## import projects.models 
from projects.models import Project

## A database query returns a collection of all objects that match the query, known as a Queryset. In this case, you want all objects in the table, so it will return a collection of all projects
def project_index(request):
    projects = Project.objects.all()  ##In line 5, you perform a query. A query is simply a command that allows you to create, retrieve, update, or delete objects (or rows) in your database
    context = {              ## In line 6 of the code block above, we define a dictionary context. The dictionary only has one entry projects to which we assign our Queryset containing all projects
        'projects': projects
    }
    return render(request, 'project_index.html', context)       ## In line 9, context is added as an argument to render(). Any entries in the context dictionary are available in the template, as long as the context argument is passed to render()
# Create your views here.

## Next, you’ll need to create the project_detail() view function. This function will need an additional argument: the id of the project that’s being viewed.
def project_detail(request, pk): ## In line 14, we perform another query. This query retrieves the project with primary key, pk, equal to that in the function argument. We then assign that project in our context dictionary, which we pass to render()
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)