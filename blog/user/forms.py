from django import forms
from . models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        labels = {
            'title':'Enter Title',
            'image':'Select Image',
            'content':'Enter Content'
        }
