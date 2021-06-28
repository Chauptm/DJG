from django.forms import fields
from uploadModel.models import uploadForm
from django import forms
# from .models import uploadForm
class upload_Form(forms.Form):
    # class Meta:
    #     model = uploadForm
    #     fields= ['title', 'image','body']
    title= forms.CharField(max_length=255)
    image=  forms.FileField()
    body=  forms.CharField(widget=forms.Textarea)