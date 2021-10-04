from django.urls import path
from . import views



app_name = 'pytutorial'

urlpatterns = [
    path('pythontutorials/list/', views.PostListView.as_view(), name='post_list'),
    path('pythontutorials/list/<slug>/', views.PostListView2.as_view(), name='post_list2'),
    path('pythontutorials/<int:pk>/', views.PostDetailView.as_view(), name='single-detail'),
    #path('python-home/', views.PythonView.as_view(), name='python-home'),
    path('index/', views.IndexView.as_view(), name='index'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('upload_image/', views.upload_image),
]
