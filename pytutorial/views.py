from django.shortcuts import render
from .models import Post, ContentBlock
from django.views.generic import TemplateView
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.views.generic.detail import SingleObjectMixin


# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = 'pytutorial/python_post.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['unique_posts'] = Post.objects.distinct()
    #     return context

class PostListView2(ListView):
    model = Post
    template_name = 'pytutorial/python_post2.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['single_post'] = Post.objects.get(id=self.kwargs['pk'])
        return context



class PostDetailView(DetailView):
    model = ContentBlock
    template_name = 'pytutorial/python_detail.html'
    context_object_name = 'post_contents'


class PythonView(TemplateView):
    template_name = "pytutorial/python_home.html"

class IndexView(TemplateView):
    template_name = "pytutorial/index.html"
