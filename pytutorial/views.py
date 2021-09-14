from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import PostForm
from django.urls import reverse_lazy
from django.utils import timezone




class PythonView(TemplateView):
    template_name = "pytutorial/python_home.html"

class IndexView(TemplateView):
    template_name = "pytutorial/index.html"


class PostListView(ListView):
    model = Post
    template_name = 'pytutorial/python_list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(PostListView, self).get_context_data(**kwargs)
    #     # Add in a QuerySet
    #     context['single_posts'] = Post.objects.get(slug=self.kwargs.get('slug'))
    #     return context

class PostListView2(ListView):
    model = Post
    template_name = 'pytutorial/python_list2.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostListView2, self).get_context_data(**kwargs)
        # Add in a QuerySet
        context['single_posts'] = Post.objects.get(slug=self.kwargs.get('slug'))
        return context


class PostDetailView(DetailView):
    model = Post
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
    redirect_field_name = 'pytutorial/python_detail.html'
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(SuperUserRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'pytutorial/python_detail.html'
    form_class = PostForm
    model = Post


class PostDeleteView(SuperUserRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('pytutorial:post_list')
    # def get_success_url(self, **kwargs):
    #     # obj = form.instance or self.object
    #     return reverse_lazy("pytutorial:post_list", kwargs={'slug': self.object.slug})




class DraftListView(SuperUserRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'pytutorial/post_draft_list.html'
    model = Post
    template_name = 'pytutorial/post_draft_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DraftListView, self).get_context_data(*args, **kwargs)
        context['drafts'] = Post.objects.filter(published_date__isnull=True).order_by('created_at')
        return context


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('pytutorial:single-detail', pk=pk)
