from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'authors', 'featured_content', 'body', 'image')
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'authors' : forms.Select(attrs={'class': 'form-control'}),
            'featured_content' : forms.TextInput(attrs={'class': 'form-control'}),
            'body' : forms.Textarea(attrs={'class': 'form-control'}),
        }