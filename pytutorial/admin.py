from django.contrib import admin
from .models import Post
from tinymce_filebrowser.admin import MCEFilebrowserAdmin

class MyModelAdmin(MCEFilebrowserAdmin):
    pass

admin.site.register(Post, MyModelAdmin)
# Register your models here.
#admin.site.register(Post)
