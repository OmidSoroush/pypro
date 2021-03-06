from django.urls import path
from . import views

##

app_name = 'blog'

urlpatterns = [
    path('', views.HomePage.as_view(), name='blog-home'),
    path('about/', views.AboutPage.as_view(), name='blog-about'),
    path('tutorial/selection/', views.TutorialsPage.as_view(), name='blog-tutorials'),
]
