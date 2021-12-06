from django.urls import path
from . import views



app_name = 'dataEngineering'

urlpatterns = [
    path('dataEngineering/list/', views.PostListView.as_view(), name='post_list'),
    path('dataEngineering/<slug>/', views.PostListView2.as_view(), name='post_list2'),
    path('dataEngineering/detail/<int:pk>/', views.PostDetailView.as_view(), name='single-detail'),
    #path('python-home/', views.PythonView.as_view(), name='python-home'),
    path('dataEngineering/post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('dataEngineering/post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('dataEngineering/drafts/page/', views.DraftListView.as_view(), name='post_draft_list'),
    path('dataEngineering/post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('dataEngineering/post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('upload_image/', views.upload_image),
]
