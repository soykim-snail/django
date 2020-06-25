from django.db import models
from django.conf import settings
# pypi에서 imagekit 사용함
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from imagekit.processors import ResizeToFit

# Create your models here.
class Post(models.Model):
    content = models.CharField(max_length=200)
    # 포스팅을 작성한 사람
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField()
    image = ProcessedImageField(upload_to='media',
                                processors=[ResizeToFit(100, 100)],
                                format='JPEG',
                                options={'quality': 60})
    # 포스팅을 좋아한 사람들
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')

    # User.post_set = 어떤 유저가 작성한 글들 (FK)
    # ~~ User.post_set = 어떤 유저가 좋아한 글들 (MtoM) ~~
    # 충돌이 나니 이름을 바꾸자 --> (related_name= 설정 옵셥으로) 
    # User.like_posts = 어떤 유저가 좋아한 글들 (MtoM) 

    class Meta:
        ordering = ['-id']  