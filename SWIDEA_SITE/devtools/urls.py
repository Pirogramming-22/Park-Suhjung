from django.urls import path
from . import views

urlpatterns = [
    path('', views.devtool_list, name='devtool_list'),           # 개발툴 목록 페이지
    path('<int:pk>/', views.devtool_detail, name='devtool_detail'), # 개발툴 상세 페이지
    path('create/', views.devtool_create, name='devtool_create'),  # 개발툴 생성 페이지
    path('<int:pk>/update/', views.devtool_update, name='devtool_update'), # 개발툴 수정 페이지
    path('<int:pk>/delete/', views.devtool_delete, name='devtool_delete'), # 개발툴 삭제 페이지
]
