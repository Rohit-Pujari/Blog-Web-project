# forms.py
from django import forms
from tinymce.widgets import TinyMCE
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content' ]
        widgets = {
            'content': TinyMCE(),
        }
