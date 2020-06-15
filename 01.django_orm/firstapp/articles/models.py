from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터베이스의 최초 생성일
    updated_at = models.DateTimeField(auto_now=True) # 데이터 최신 수정일

