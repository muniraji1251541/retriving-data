from django.shortcuts import render
from application.models import *
# Create your views here.

def topics(request):
    qst=Topic.objects.all()
    d={'topics':qst}
    return render(request,'topics.html',d)

def webpages(request):
    qsw=Webpage.objects.all()
    d={'webpages':qsw}
    return render(request,'webpages.html',d)

def access(request):
    qsa=AccessRecord.objects.all()
    d={'access':qsa}
    return render(request,'access.html',d)