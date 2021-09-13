from django.contrib import admin
from .models import Post, ContentBlock
from .forms import *


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm


# Register your models here.
admin.site.register(ContentBlock, BlogAdmin)
admin.site.register(Post)
