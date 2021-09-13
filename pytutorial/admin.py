from django.contrib import admin
from .models import Post, ContentBlock


@admin.register(ContentBlock)
class PostAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Post)
