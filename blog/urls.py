from django.urls import path
from . import views



urlpatterns = [
    path('', views.HomePage.as_view(), name='blog-home'),
    path('', views.AboutPage.as_view(), name='blog-about'),
]
