from django.contrib import admin
from .models import MLPost


@admin.register(MLPost)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']

    class Media:
        js = [
            '/static/blog/tinymce/tinydefault.js',
            '/static/blog/tinymce/jquery.tinymce.min.js',
            '/static/blog/tinymce/tinymce.min.js',
        ]
