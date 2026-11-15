from django import forms
from .models import *
class postForm(forms.ModelForm):
    class Meta:
        model = postModel
        fields = ('heading','texts','image')