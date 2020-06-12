"""firstapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from articles import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('dinner/', views.dinner),
    path('photo/', views.photo),
    # path('hello/<str:name>/', views.hello)
    path('hello/<name>/', views.hello), # str 타입선언은 생략 가능
    path('intro/<name>/<int:age>', views.intro),
    path('gugu/<int:num1>/<int:num2>/', views.gugu),
    path('dtl-practice/', views.dtl_practice),
    path('word/<word>/', views.word_check),
    path('throw/', views.throw),
    path('catch/', views.catch),    
]
