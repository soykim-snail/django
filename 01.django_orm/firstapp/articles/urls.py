from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'), # 글작성
    path('create/', views.create, name='create'), # 글저장
    path('<int:pk>/', views.detail, name='detail'), # 글보기
    path('<int:pk>/delete/', views.delete, name='delete'), # 삭제
    path('<int:pk>/edit/', views.edit, name='edit'), # 글수정
    path('<int:pk>/update/', views.update, name='update'), # 수정저장
]
