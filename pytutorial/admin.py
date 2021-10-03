from django.contrib import admin
from .models import Post


@admin.register(Post)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']

    class Media:
        js = [
            'blog/tinymce/jquery.tinymce.min.js',
            'blog/tinymce/tinymce.min.js',
            'blog/tinymce/tinydefault.js',
        ]

# Register your models here.
#admin.site.register(Post)
