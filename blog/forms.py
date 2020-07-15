from django import forms

from .models import BlogPost


class CreateBlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title', 'author', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
