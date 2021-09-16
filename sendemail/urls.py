# sendemail/urls.py
from django.urls import path
from .views import contactView, successView


app_name = 'sendemail'


urlpatterns = [
    path('contact/', contactView, name='contact'),
    path('success/', successView.as_view(), name='success'),
]
