from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    video = models.FileField(upload_to='videos')
    description = models.TextField()

