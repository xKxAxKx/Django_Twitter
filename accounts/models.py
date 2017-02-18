from django.db import models
from django.contrib.auth.models import User

class Ex_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=100)
    image_file = models.CharField(max_length=100)
    profile = models.TextField(max_length=140)
