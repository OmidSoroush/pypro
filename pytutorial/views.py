from django.shortcuts import render, get_object_or_404
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
    #     context = super(PostListView, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['unique_posts'] = Post.objects.filter(id=self.kwargs.get('pk'))
    #     return context


class PostListView2(ListView):
    model = Post
    template_name = 'pytutorial/python_post2.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    # def get_queryset(self):
    #     return Post.objects.filter(author=self.request.user)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostListView2, self).get_context_data(**kwargs)
        # Add in a QuerySet
        #context['unique_posts'] = Post.objects.get(slug=self.kwargs.get('slug'))
        context['unique_posts'] = ContentBlock.objects.select_related('post').get(slug=self.kwargs.get('slug'))
        return context



class PostDetailView(DetailView):
    model = ContentBlock
    template_name = 'pytutorial/python_detail.html'
    context_object_name = 'post_contents'

    # get a list of all (by default DetailView provides singlewise data)
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['unique_title'] = ContentBlock.objects.all().values('post').distinct()
        context['content_list'] = ContentBlock.objects.all()
        return context


class PythonView(TemplateView):
    template_name = "pytutorial/python_home.html"

class IndexView(TemplateView):
    template_name = "pytutorial/index.html"
