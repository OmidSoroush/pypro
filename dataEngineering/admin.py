from django.contrib import admin
from .models import DataEngineeringPost


@admin.register(DataEngineeringPost)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']

    class Media:
        js = [
            '/static/blog/tinymce/tinydefault.js',
            '/static/blog/tinymce/jquery.tinymce.min.js',
            '/static/blog/tinymce/tinymce.min.js',
        ]
