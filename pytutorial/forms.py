from django import forms
from .models import ContentBlock



class PostForm(forms.ModelForm):
    class Meta:
        model = ContentBlock
        fields = ('post', 'subtitle', 'sub_content')

        widgets = {
            'post': forms.TextInput(attrs={'class': 'textinputclass'}),
            'subtitle': forms.Textarea(attrs={'class': 'postcontent'}),
        }

#client id: 8c5f651e0834ce0
#client secret: 8c86f1991295ff288c4ed3f28b65a729fc50de62
