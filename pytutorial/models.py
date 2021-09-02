from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class PythonPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)
    author = models.ForeignKey(User, related_name='pythonposts', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('python-post-single', kwargs={'pk': self.pk})

    class Meta:
        ordering = ["-created_at"]
