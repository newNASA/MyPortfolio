from django.shortcuts import render, get_object_or_404
from .models import My_info, My_skills, Interests, My_projects

# Create your views here.

def home(request):
    my_info = My_info.objects.first()
    my_skills = My_skills.objects.all()
    my_interests = Interests.objects.all()
    my_projects = My_projects.objects.all()

    context = {
        "my_info": my_info,
        "my_skills": my_skills,
        "my_interests": my_interests,
        "my_projects": my_projects
    }
    return render(request, 'index.html', context)

def detail(request, id):
    project = get_object_or_404(My_projects, id=id)
    context = {
        "project": project,
    }
    return render(request, 'portfolio-details.html', context)
