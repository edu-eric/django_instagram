from django.db import models
from django.conf import settings

def image_upload_path():
    return f'article/%Y/%m/%d/'

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to=image_upload_path(), blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)