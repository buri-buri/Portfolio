from django.shortcuts import render
from django.conf import settings
def index(request):
    developer='Sagar Shivam Kaushik'
    d={
        'developer':developer,
        'name':settings.DATA['NAME'],
        'about_me':settings.DATA['ABOUT_ME']
    }
    return render(request,'main/index.html',d)
def project(request):
    d={
        'project':settings.DATA['PROJECTS']
    }
    return render(request,'main/project.html',d)
def language(request):
    d={
        'language':settings.DATA['LANGUAGE']
    }
    return render(request,'main/language.html',d)
