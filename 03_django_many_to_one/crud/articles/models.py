from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # comment_set ... 칼럼이 자동 생성됨

# 댓글 테이블 추가
class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Foreign key 설정, 연결하려는 모델, on_delete 값
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article 객체 칼럼이 생성됨
    # article_id ... 칼럼이 자동 생성됨
    
    