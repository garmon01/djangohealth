from django.shortcuts import render
from .models import Disorder
from django.http import HttpResponse

# Create your views here.
def disorders_list(request):
    disorders = Disorder.objects.all().order_by('title')
    return render(request, 'disorders/disorders_list.html', {'disorders': disorders} ) 

def disorders_detail(request, slug):
    #return HttpResponse(slug)
    disorder = Disorder.objects.get(slug=slug)
    return render(request, 'disorders/disorders_detail.html', {'disorder': disorder})