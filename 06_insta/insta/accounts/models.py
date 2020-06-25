from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# User 확장을 미리 해 놓는 것을 권장함
class User(AbstractUser):
    pass
