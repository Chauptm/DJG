from django.db.models import fields
from django import forms
# from .models import sp

# class sp_Form(forms.ModelForm):
#     class Meta:
#         model = sp
#         fields = ['name', 'logo']

class sp_Form(forms.Form):
    name= forms.CharField(widget=forms.Textarea)
    logo= forms.CharField(widget=forms.Textarea)