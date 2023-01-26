from django.shortcuts import render
from application.models import *
from django.db.models.functions import Length
from django.db.models import Q
# Create your views here.

def topics(request):
    qst=Topic.objects.all()
    d={'topics':qst}
    return render(request,'topics.html',d)

def webpages(request):
    qsw=Webpage.objects.all()
    qsw=Webpage.objects.filter(topic_name='Cricket')
    qsw=Webpage.objects.filter(topic_name='Rugby')
    qsw=Webpage.objects.exclude(topic_name='Cricket')
    qsw=Webpage.objects.all()[:5:]
    qsw=Webpage.objects.all().order_by('name')
    qsw=Webpage.objects.all().order_by('-name')
    qsw=Webpage.objects.filter(topic_name='Cricket').order_by('name')
    qsw=Webpage.objects.all().order_by(Length('name'))
    qsw=Webpage.objects.all().order_by(Length('name').desc())
    qsw=Webpage.objects.filter(name__startswith='muni')
    qsw=Webpage.objects.filter(name__endswith='i')
    qsw=Webpage.objects.all()
    qsw=Webpage.objects.filter(name__contains='i')
    qsw=Webpage.objects.filter(name__regex='\w{6}')
    qsw=Webpage.objects.filter(name__in=['Abishek','Muniraji','Loganathan'])
    qsw=Webpage.objects.filter(Q(topic_name='Cricket') | Q(name='Simbu'))
    qsw=Webpage.objects.filter(Q(topic_name='Foot Ball') & Q(name='Tharun'))
    qsw=Webpage.objects.filter(Q(topic_name='Foot Ball') & Q(name__contains='a'))
    d={'webpages':qsw}
    return render(request,'webpages.html',d)

def access(request):
    qsa=AccessRecord.objects.all()
    qsa=AccessRecord.objects.filter(date='2003-4-9')
    qsa=AccessRecord.objects.filter(date__gt='2003-4-9')
    qsa=AccessRecord.objects.filter(date__gte='2003-4-9')
    qsa=AccessRecord.objects.filter(date__lt='2003-4-9')
    qsa=AccessRecord.objects.filter(date__lte='2003-4-9')
    qsa=AccessRecord.objects.all()
    qsa=AccessRecord.objects.filter(date__year='2000')
    qsa=AccessRecord.objects.filter(date__month='9')
    qsa=AccessRecord.objects.filter(date__day='27')
    qsa=AccessRecord.objects.filter(date__year__gt='2000')
    qsa=AccessRecord.objects.filter(date__year__gte='2000')
    d={'access':qsa}
    return render(request,'access.html',d)