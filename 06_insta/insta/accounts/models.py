from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

# User 확장을 미리 해 놓는 것을 권장함
class User(AbstractUser):
    # 사용자가 팔로잉 하는 사람들 (팔로잉 당하는 사람에게는 follower 필드가 생성됨)
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='follower')
    image = ProcessedImageField(upload_to='accounts', # upload_to 삭제해도 됨
                                processors=[ResizeToFill(100, 100)],
                                format='JPEG',
                                options={'quality': 60},
                                default='default.jpg',
                                )