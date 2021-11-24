from django.urls import path
from . import views



app_name = 'pyspark'

urlpatterns = [
    path('pyspark/list/', views.PostListView.as_view(), name='post_list'),
    path('pyspark/<slug>/', views.PostListView2.as_view(), name='post_list2'),
    path('pyspark/detail/<int:pk>/', views.PostDetailView.as_view(), name='single-detail'),
    #path('python-home/', views.PythonView.as_view(), name='python-home'),
    path('pyspark/post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('pyspark/post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('pyspark/drafts/page/', views.DraftListView.as_view(), name='post_draft_list'),
    path('pyspark/post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('pyspark/post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('upload_image/', views.upload_image),
]
