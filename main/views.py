from django.shortcuts import render
def index(request):
    developer='Sagar Shivam Kaushik'
    d={'developer':developer}
    return render(request,'main/index.html',d)
def project(request):
    d=dict()
    return render(request,'main/project.html',d)
def language(request):
    d=dict()
    return render(request,'main/language.html',d)
