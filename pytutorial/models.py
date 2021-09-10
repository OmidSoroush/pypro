from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

import misaka

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateField(auto_now=True)
    author = models.ForeignKey(User, related_name='pythonposts', on_delete=models.CASCADE)
    slug = models.SlugField(allow_unicode=True, unique=True, blank=True)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        self.slug = slugify(self.created_at)
        self.title_html = misaka.html(self.title)
        super().save(*args, **kwargs)


    # def get_absolute_url(self):
    #     return reverse('pytutorial:single-subtitle', kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-created_at"]



class ContentBlock(models.Model):
    """ A block with additionnal subtitle and content for posts """
    post = models.ForeignKey(Post, related_name='contentblocks', on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=200)
    sub_content = models.TextField()
    created_at = models.DateField(auto_now=True)
    slug = models.SlugField(allow_unicode=True, max_length=200, blank=True)

    def __str__(self):
        return self.subtitle

    def save(self, *args, **kwargs):
        self.slug = slugify(self.subtitle)
        self.subtitle_html = misaka.html(self.subtitle)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pytutorial:single-detail', kwargs={'slug': self.slug})
