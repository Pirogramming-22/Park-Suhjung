
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_new/', views.post_new, name='post_new'),
    path('like_post/',views.like_post, name="like_post"),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/comment/', views.add_comment, name='add_comment'), 
    path('post/comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
] 
