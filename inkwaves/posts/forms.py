from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'announcement', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post title'
            }),
            "announcement": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Post announcement'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Publish date'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Post text'
            })
        }