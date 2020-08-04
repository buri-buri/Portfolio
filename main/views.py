from django.shortcuts import render

def index(request):
    d=dict()
    return render(request,'main\index.html',d)