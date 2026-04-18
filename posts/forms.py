









from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title','body','slug','banner']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'my-custom-class form-control'}),
            'body': forms.Textarea(attrs={'class': 'mx-width form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'banner': forms.FileInput(attrs={'class': 'form-control'}),
        }
