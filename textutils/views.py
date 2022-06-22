# I have created this file - Samrat

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request, 'index.html')

def removepunc(request):
     djtext = request.GET.get('text', 'default')
     print(djtext)
     return HttpResponse("remove punc")

def capfirst(request):
     return HttpResponse("Capitalize first")

def newlineremove(request):
     return HttpResponse("New line remove")

def spaceremove(request):
     return HttpResponse("Space remove")

def charcount(request):
     return HttpResponse("charcount")