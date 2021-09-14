from django import forms
from .models import Post



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
        }

#client id: 8c5f651e0834ce0
#client secret: 8c86f1991295ff288c4ed3f28b65a729fc50de62
