from django.urls import path
from . import views

urlpatterns = [
    path('idea/<int:pk>/toggle-star/', views.toggle_star, name='toggle_star'),
    #path('api/idea/<int:idea_id>/adjust-interest/', views.adjust_interest, name='adjust_interest'),
    path("idea/<int:pk>/adjust-interest/", views.adjust_interest, name="adjust_interest"),

]