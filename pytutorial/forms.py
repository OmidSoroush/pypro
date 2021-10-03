from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget


#client id: 8c5f651e0834ce0
#client secret: 8c86f1991295ff288c4ed3f28b65a729fc50de62
class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = ('title', 'content')
