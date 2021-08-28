from django.shortcuts import render
from .models import About, Intro, Projects, Skills

def home(request):
    intro_date = Intro.objects.all()[0]
    projects_data = Projects.objects.all()
    skills_data = Skills.objects.all

    context = {
        'intro': intro_date,
        'projects': projects_data,
        'skills': skills_data,
    }
    return render(request, 'Index/index.html', context)

def about(request):
    about_data = About.objects.all()[0]
    skills_data = Skills.objects.all

    context = {
        'about': about_data,
        'skills': skills_data,
    }
    return render(request, 'Index/about.html', context)

