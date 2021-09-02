from django.urls import path
from . import views

app_name = 'pytutorial'

urlpatterns = [
    path('pythontutorials/', views.PythonPostListView.as_view(), name='python-home'),
    path('pythontutorials/<int:pk>/', views.PythonPostDetailView.as_view(), name='python-post-single'),
]
