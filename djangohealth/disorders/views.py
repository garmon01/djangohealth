from django.shortcuts import render
from .models import Disorder

# Create your views here.
def disorders_list(request):
    disorders = Disorder.objects.all().order_by('title')
    return render(request, 'disorders/disorders_list.html', {'disorders': disorders} ) 