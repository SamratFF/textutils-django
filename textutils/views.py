# I have created this file - Samrat

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return render(request, 'index.html')

def analyze(request):
     djtext = request.GET.get('text', 'Please Enter some text to show here')

     removepunc = request.GET.get('removepunc', 'off')
     capitalizefirst = request.GET.get('capitalizefirst', 'off')

     # punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
     punctuations_list = ['!', '(', ')', '-', '[', ']', '{', '}', ';', ':', "'", '"', '\\', ',', '<', '>', '.', '/', '?', '@', '#', '$', '%', '^', '&', '*', '_', '~']


     if removepunc == 'on':
          analyzed = ""


          for char in djtext:
               if char not in punctuations_list:
                    analyzed = analyzed + char

          params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
          return render(request, 'analyze.html', params)
     else:
          return HttpResponse("Error")