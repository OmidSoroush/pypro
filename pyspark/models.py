from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from tinymce.models import HTMLField
import misaka
import datetime



class PysparkPost(models.Model):
    author = models.ForeignKey(User, related_name='pysparkposts', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = HTMLField(null=True)
    created_at = models.DateTimeField(editable=True, auto_now_add=True)
    slug = models.SlugField(allow_unicode=True, max_length=200, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['pk']

    def publish(self):
        self.published_date = datetime.date.today()
        self.save()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.title_html = misaka.html(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('pyspark:single-detail', kwargs={'pk': self.pk})
