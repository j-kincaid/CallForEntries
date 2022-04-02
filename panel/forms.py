from django import forms

from .models import Panel

class PanelForm(forms.ModelForm):
    class Meta:
        model = Panel
        fields = ('full_name', 'medium', 'bio')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'medium':forms.Textarea(attrs={'class': 'form-control mb-5'})
        }
        labels = {
            'full_name': "Please write your full name."
            # 'medium': "What is your medium? Select more than one, if applicable.",
            # 'bio': "Please include a brief biography (200 characters max)."
        }

