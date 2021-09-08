from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='blog-home'),
    path('about/', views.AboutPage.as_view(), name='blog-about'),
    path('tutorials/', views.TutorialsPage.as_view(), name='blog-tutorials'),
]
