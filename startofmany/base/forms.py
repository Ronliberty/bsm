from django import forms
from .models import HeroContent, GalleryItem, PricingPlan, AboutSection, ContactInfo

class HeroContentForm(forms.ModelForm):
    class Meta:
        model = HeroContent
        fields = ['title', 'subtitle', 'cta_text', 'cta_link']
        widgets = {
            'title': forms.TextInput(attrs={
                'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px;'
            }),
            'subtitle': forms.TextInput(attrs={
                'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px;'
            }),
            'cta_text': forms.TextInput(attrs={
                'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px;'
            }),
            'cta_link': forms.URLInput(attrs={
                'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px;'
            }),
        }

class GalleryItemForm(forms.ModelForm):
    class Meta:
        model = GalleryItem
        fields = ['video']
        widgets = {
            'video': forms.FileInput(attrs={
                'style': 'border: 2px solid #ccc; padding: 10px; margin: 5px; color: red; width: 70%;',  # Example inline CSS
                'class': 'custom-file-input',  # Optional: Add a class for additional styling
            }),
        }

class PricingPlanForm(forms.ModelForm):
    class Meta:
        model = PricingPlan
        fields = ['name', 'price', 'features']
        widgets = {
            'name': forms.TextInput(
                attrs={'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px;'}),
            'price': forms.NumberInput(
                attrs={'style': 'width: 100%; padding: 10px; border: 1px solid #ccc; border-radius: 4px;'}),
            'features': forms.Textarea(attrs={
                'style': 'width: 100%; height: 100px; padding: 10px; border: 1px solid #ccc; border-radius: 4px;'}),
        }

class AboutSectionForm(forms.ModelForm):
    class Meta:
        model = AboutSection
        fields = ['description', 'location', 'phone', 'email']
        widgets = {
            'description': forms.Textarea(attrs={'style': 'width: 90%; margin-left: 10px; height: 150px; margin-bottom: 15px; margin-top: 15px; border: 1px solid #ccc; padding: 10px; border-radius: 10px;'}),
            'location': forms.TextInput(attrs={'style': 'width: 80%; margin-left: 10px; margin-bottom: 10px; margin-top: 10px; border: 1px solid #ccc; padding: 10px; border-radius: 10px;'}),
            'phone': forms.TextInput(attrs={'style': 'width: 80%; margin-left: 10px; margin-bottom: 10px; margin-top: 10px; border: 1px solid #ccc; padding: 10px; border-radius: 10px;'}),
            'email': forms.EmailInput(attrs={'style': 'width: 80%; margin-left: 10px; margin-bottom: 15px; margin-top: 10px; border: 1px solid #ccc; padding: 10px; border-radius: 10px;'}),
        }

class ContactInfoForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = ['address', 'phone', 'email']
        widgets = {
                    'address': forms.TextInput(attrs={'style': 'width: 80%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px;'}),
                    'phone': forms.TextInput(attrs={'style': 'width: 80%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px;'}),
                    'email': forms.EmailInput(attrs={'style': 'width: 80%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px;'}),
                }