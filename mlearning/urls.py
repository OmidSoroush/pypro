from django.urls import path
from . import views



app_name = 'mlearning'

urlpatterns = [
    path('machinelearning/list/', views.PostListView.as_view(), name='post_list'),
    path('machinelearning/<slug>/', views.PostListView2.as_view(), name='post_list2'),
    path('machinelearning/<int:pk>/', views.PostDetailView.as_view(), name='single-detail'),
    #path('python-home/', views.PythonView.as_view(), name='python-home'),
    path('ml/post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('ml/post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('ml/drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('ml/post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('ml/post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('upload_image/', views.upload_image),
]
