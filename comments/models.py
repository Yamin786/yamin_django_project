from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class comment_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_description = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/',blank=True , null=True)