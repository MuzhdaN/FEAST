from django.shortcuts import render
from django.views.generic import TemplateView


class home(TemplateView):
    '''
    this will view home page
    '''
    template_name = 'home/index.html'
