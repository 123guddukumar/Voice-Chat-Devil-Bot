from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    output = models.TextField(default="Ok")
    timestamp = models.DateTimeField(auto_now_add=True)    
