from django.shortcuts import render
from django.views.generic import TemplateView

# Home page
class HomePage(TemplateView):
    template_name = 'blog/home.html'

# About page
class AboutPage(TemplateView):
    template_name = 'blog/about.html'

# tutorials page
class TutorialsPage(TemplateView):
    template_name = 'blog/tutorials.html'
