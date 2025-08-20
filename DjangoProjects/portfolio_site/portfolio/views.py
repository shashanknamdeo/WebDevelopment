from django.shortcuts import render
from .models import Project, Certificate

def home(request):
    projects = Project.objects.all()
    certificates = Certificate.objects.all()
    return render(request, "home.html", {"projects": projects, "certificates": certificates})
