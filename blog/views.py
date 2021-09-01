from django.shortcuts import render
from django.views.generic import TemplateView

# Home page
class HomePage(TemplateView):
    template_name = 'blog/base.html'

# About page
class AboutPage(TemplateView):
    template_name = 'about.html'
