from django import forms
from .models import SQLPost
from tinymce.widgets import TinyMCE


#client id: 8c5f651e0834ce0
#client secret: 8c86f1991295ff288c4ed3f28b65a729fc50de62
class SQLPostForm(forms.ModelForm):

    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = SQLPost
        fields = ('title', 'content')
        js = [
            '/static/blog/tinymce/tinydefault.js',
            '/static/blog/tinymce/jquery.tinymce.min.js',
            '/static/blog/tinymce/tinymce.min.js',
        ]
