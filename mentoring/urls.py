# mentoring/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('instructor/', views.instructor, name='instructor'),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('reviews/', views.reviews, name='reviews'),
    path('faq/', views.faq, name='faq'),
    path('apply/', views.apply, name='apply'),
]