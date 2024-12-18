from django.shortcuts import render
from django.views.generic import TemplateView, ListView , DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.

class baseview(TemplateView):
    #Template folder already defined in settings.py so you dont have to specify that folder in views
    template_name = 'base.html'

class homeview(TemplateView):
    template_name = 'home.html'

class indexview(TemplateView):
    template_name = 'index.html'

# Template_Container 

class conindexview(TemplateView):
    template_name = 'container/index.html'
