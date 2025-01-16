from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class reviews:
        class Meta:
            model = Post
            fields = ['title', 'text', 'year', 'star', 'genre','pd','actors','running_time']
