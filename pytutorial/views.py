from django.shortcuts import render, get_object_or_404
from .models import Post, ContentBlock
from django.views.generic import TemplateView
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostForm



# Create your views here.
# class PostListView(ListView):
#     model = Post
#     template_name = 'pytutorial/python_post.html'
#     context_object_name = 'posts'
#     ordering = ['-created_at']

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(PostListView, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['unique_posts'] = Post.objects.filter(id=self.kwargs.get('pk'))
    #     return context

# class PostListView2(ListView):
#     model = Post
#     template_name = 'pytutorial/python_post2.html'
#     context_object_name = 'posts'
#     ordering = ['-created_at']
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super(PostListView2, self).get_context_data(**kwargs)
#         # Add in a QuerySet
#         context['unique_posts'] = ContentBlock.objects.select_related('post').get(slug=self.kwargs.get('slug'))
#         return context



class PostDetailView(DetailView):
    model = ContentBlock
    template_name = 'pytutorial/python_detail.html'
    context_object_name = 'post_contents'

    # get a list of all (by default DetailView provides singlewise data)
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.all()
        #context['content_list'] = ContentBlock.objects.all()
        #context['b'] = ContentBlock.objects.select_related('post').all() # Forward ForeignKey relationship
        #context['a'] = Post.objects.prefetch_related('contentblocks').all()
        return context



class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class CreatePostView(SuperUserRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm
    model = ContentBlock


class PythonView(TemplateView):
    template_name = "pytutorial/python_home.html"

class IndexView(TemplateView):
    template_name = "pytutorial/index.html"
