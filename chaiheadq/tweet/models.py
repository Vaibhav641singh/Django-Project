from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # lowercase 'user'
    text = models.TextField(max_length=240)
    photo = models.ImageField(upload_to="photos/", blank=True, null=True)  # fixed typo: ImageFeild → ImageField
    created_at = models.DateTimeField(auto_now_add=True)  # fixed typo: DataTimeField → DateTimeField
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:10]}"
