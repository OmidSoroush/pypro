from django.shortcuts import render
from .models import Post, ContentBlock
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)


# Create your views here.
class PostListView(ListView):
    model = ContentBlock
    template_name = 'pytutorial/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class PostDetailView(DeleteView):
    model = ContentBlock
    template_name = 'pytutorial/post_detail.html'
    context_object_name = 'post_contents'
