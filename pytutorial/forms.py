from django import forms
from .models import ContentBlock


class BlogAdminForm(forms.ModelForm):
    sub_content = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))

    class Meta:
        model = ContentBlock
        fields = ('post', 'subtitle', 'sub_content')
