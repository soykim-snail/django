from django.urls import path
from . import views   # '.'란, 현재 위치에서 임포트

# articles앱의 url만 가져온다.
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'), # articles/로 넘어온다. 
    path('dinner/', views.dinner, name='dinner'),
    path('photo/', views.photo, name='photo'),
    # path('hello/<str:name>/', views.hello)
    path('hello/<name>/', views.hello, name='hello'), # str 타입선언은 생략 가능
    path('intro/<name>/<int:age>', views.intro, name='intro'),
    path('gugu/<int:num1>/<int:num2>/', views.gugu, name='gugu'),
    path('dtl-practice/', views.dtl_practice, name='dtl-practice'),
    path('word/<word>/', views.word_check, name='word'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),   
    # 이름을 입력하면, 랜덤 숫자를 뽑아준다.
    path('draw/', views.draw, name='draw'),
    path('show/', views.show, name='show'),
    path('artii/', views.artii, name='artii'),
    path('artii-result/', views.artii_result, name='artii_result'),
    path('artii-drop/', views.artii_drop, name='artii_drop'),
    path('artii-result-drop/', views.artii_result_drop, name='artii_result_drop'),
]
