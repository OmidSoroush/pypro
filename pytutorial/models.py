from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateField(auto_now=True)
    author = models.ForeignKey(User, related_name='pythonposts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pytutorial:single-post', kwargs={'pk': self.pk})

    class Meta:
        ordering = ["-created_at"]



class ContentBlock(models.Model):
    """ A block with additionnal subtitle and content for posts """
    post = models.ForeignKey(Post, related_name='contentblocks', on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=200)
    sub_content = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.subtitle

    def get_absolute_url(self):
        return reverse('pytutorial:single-subtitle', kwargs={'pk': self.pk})
