from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from django.http import HttpResponse
from .form import upload_Form
from .models import uploadForm
# Create your views here.

def uploadFile(request):
    uL= upload_Form
    return render(request, 'uploadModel/uploadForm.html', {'uL': uL})

def getFile(request):
    form =upload_Form(request.POST, request.FILES)
    if form.is_valid():
        instance = uploadForm(image=request.FILES['image'], title= request.POST['title'], body= request.POST['body'])
        instance.save()
        return HttpResponse('Lưu thành công')
    else: 
        return HttpResponse('Không thành công')
