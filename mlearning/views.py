from django.shortcuts import render, get_object_or_404, redirect
from .models import MLPost
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import MLPostForm
from django.urls import reverse_lazy
from django.utils import timezone




class PostListView(ListView):
    model = MLPost
    template_name = 'mlearning/post_list.html'
    context_object_name = 'posts'
    ordering = ['created_at']

    def get_queryset(self):
        return MLPost.objects.filter(published_date__lte=timezone.now())

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(PostListView, self).get_context_data(**kwargs)
    #     # Add in a QuerySet
    #     context['single_posts'] = Post.objects.get(slug=self.kwargs.get('slug'))
    #     return context

class PostListView2(ListView):
    model = MLPost
    template_name = 'mlearning/post_list2.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return MLPost.objects.filter(published_date__lte=timezone.now())

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostListView2, self).get_context_data(**kwargs)
        # Add in a QuerySet
        context['single_posts'] = MLPost.objects.get(slug=self.kwargs.get('slug'))
        return context


class PostDetailView(DetailView):
    model = MLPost
    template_name = 'mlearning/ml_detail.html'
    context_object_name = 'post_contents'

    # get a list of all (by default DetailView provides singlewise data)
    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        context['posts'] = MLPost.objects.all().order_by('created_at')
        #context['content_list'] = ContentBlock.objects.all()
        #context['b'] = ContentBlock.objects.select_related('post').all() # Forward ForeignKey relationship
        #context['a'] = Post.objects.prefetch_related('contentblocks').all()
        return context

class SuperUserRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class CreatePostView(SuperUserRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'mlearning/ml_detail.html'
    form_class = MLPostForm
    model = MLPost

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(SuperUserRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'mlearning/ml_detail.html'
    form_class = MLPostForm
    model = MLPost


class PostDeleteView(SuperUserRequiredMixin,DeleteView):
    model = MLPost
    success_url = reverse_lazy('mlearning:post_list')
    # def get_success_url(self, **kwargs):
    #     # obj = form.instance or self.object
    #     return reverse_lazy("mlearning:post_list", kwargs={'slug': self.object.slug})




class DraftListView(SuperUserRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'mlearning/ml_draft_list.html'
    model = MLPost
    template_name = 'mlearning/ml_draft_list.html'


    def get_context_data(self, *args, **kwargs):
        context = super(DraftListView, self).get_context_data(*args, **kwargs)
        context['drafts'] = MLPost.objects.filter(published_date__isnull=True).order_by('created_at')
        return context


@login_required
def post_publish(request, pk):
    post = get_object_or_404(MLPost, pk=pk)
    post.publish()
    return redirect('mlearning:single-detail', pk=pk)




import os

from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_image(request):
    if request.method == "POST":
        file_obj = request.FILES['file']
        file_name_suffix = file_obj.name.split(".")[-1]
        if file_name_suffix not in ["jpg", "png", "gif", "jpeg", ]:
            return JsonResponse({"message": "Wrong file format"})

        upload_time = timezone.now()
        path = os.path.join(
            settings.MEDIA_ROOT,
            'tinymce',
            str(upload_time.year),
            str(upload_time.month)
        )
        # If there is no such path, create
        if not os.path.exists(path):
            os.makedirs(path)

        file_path = os.path.join(path, file_obj.name)

        file_url = f'{settings.MEDIA_URL}tinymce/{upload_time.year}/{upload_time.month}/{file_obj.name}'

        if os.path.exists(file_path):
            return JsonResponse({
                "message": "file already exist",
                'location': file_url
            })

        with open(file_path, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        return JsonResponse({
            'message': 'Image uploaded successfully',
            'location': file_url
        })
    return JsonResponse({'detail': "Wrong request"})
