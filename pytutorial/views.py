from django.shortcuts import render
from .models import PythonPost
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)


# Create your views here.
class PythonPostListView(ListView):
    model = PythonPost
    template_name = 'pytutorial/python_post_list.html'
    context_object_name = 'python_posts'
    ordering = ['-created_at']


class PythonPostDetailView(DeleteView):
    model = PythonPost
    template_name = 'pytutorial/python_post_detail.html'
    context_object_name = 'python_posts'
