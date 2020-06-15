from django.db import models


# Create your models here.
class Article(models.Model):
    my_title = models.CharField(max_length=10)
    my_content = models.TextField()
    my_created_at = models.DateTimeField(auto_now_add=True)
    my_updated_at = models.DateTimeField(auto_now=True)

