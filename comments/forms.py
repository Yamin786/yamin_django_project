from django import forms
from .models import comment_model

class comment_form(forms.ModelForm):
    class Meta:
        model = comment_model
        fields = ['comment_description','photo']