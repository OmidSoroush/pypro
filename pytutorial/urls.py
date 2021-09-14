from django.urls import path
from . import views



app_name = 'pytutorial'

urlpatterns = [
    path('pythontutorials/<slug>/', views.PostDetailView.as_view(), name='single-detail_1'),
    #path('pythontutorials/post/<slug>/', views.PostListView2.as_view(), name='single-subtitle'),
    path('pythontutorials/<slug>/', views.PostDetailView.as_view(), name='single-detail'),
    path('python-home/', views.PythonView.as_view(), name='python-home'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<slug>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<slug>/publish/', views.post_publish, name='post_publish'),
]
