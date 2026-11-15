from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class postModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , null=True , blank=True)
    heading = models.CharField(max_length=255)
    texts = models.TextField(max_length=500)
    image = models.ImageField(upload_to='post_image/',null=True,blank=True)