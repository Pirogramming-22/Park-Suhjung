from django.urls import path
from .views import *
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.review_list, name='review_list'),
 
    path('create/', views.create_post, name='create_post'),
    
    path('review/<int:pk>/', views.post_detail, name='post_detail'),
  
    path('review/<int:pk>/edit/', views.review_edit, name='review_edit'),
]