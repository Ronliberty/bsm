from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'file', 'link']
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'style': 'width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc; margin-bottom: 20px;'
            }),
            'title': forms.TextInput(attrs={
                'style': 'width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc; margin-bottom: 20px;'
            }),
            'file': forms.FileInput(attrs={
                'style': 'width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc; margin-bottom: 20px;'
            }),
            'link': forms.URLInput(attrs={
                'style': 'width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc; margin-bottom: 20px;'
            }),
        }
