from django.urls import path
from .import views

urlpatterns =[
    path('', views.homeView, name = 'homepage'),
    path('about', views.aboutView, name = 'aboutpage'),
    path('contact', views.ContactView, name = 'contactpage')
]