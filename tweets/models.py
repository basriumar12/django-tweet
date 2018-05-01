from django.db import models

class Tweet(models.Model):
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
