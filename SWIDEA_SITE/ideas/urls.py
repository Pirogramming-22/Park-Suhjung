from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.idea_list, name='idea_list'),            # 아이디어 목록 페이지
    path('<int:pk>/', views.idea_detail, name='idea_detail'), # 아이디어 상세 페이지
    path('create/', views.idea_create, name='idea_create'),  # 아이디어 생성 페이지
    path('<int:pk>/update/', views.idea_update, name='idea_update'), # 아이디어 수정 페이지
    path('<int:pk>/delete/', views.idea_delete, name='idea_delete'), # 아이디어 삭제 페이지
    path('<int:pk>/like/', views.toggle_like, name='toggle_like'),
    path('<int:pk>/adjust_interest/', views.adjust_interest, name='adjust_interest'),
    path('wishlist/<int:pk>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('<int:pk>/edit/', views.idea_edit, name='idea_edit'),
    path('<int:pk>/toggle_star/', views.toggle_star, name='toggle_star'),
    path('devtool/<int:pk>/', views.devtool_detail, name='devtool_detail'),  # 개발툴 디테일 페이지
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

