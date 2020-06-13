from django.urls import path, include
from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'), # pages/ 로 넘어온다. 
]
