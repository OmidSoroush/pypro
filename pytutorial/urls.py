from django.urls import path
from . import views



app_name = 'pytutorial'

urlpatterns = [
    path('pythontutorials/', views.PostListView.as_view(), name='python-home'),
    path('pythontutorials/<int:pk>/', views.PostDetailView.as_view(), name='single-post'),
    #path('new/', views.PythonView.as_view(), name='python-home'),
    #path('index/', views.IndexView.as_view(), name='index'),
]
