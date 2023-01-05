from django.shortcuts import render
from django.views.generic import TemplateView


class home(TemplateView):
    template_name = 'home/index.html'
