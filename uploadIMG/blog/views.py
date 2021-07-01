
from django.http import request
from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from .models import listBlogForm
def list(request):
    lB= listBlogForm.objects.all()
    paginator= Paginator(lB,1)
    page_number= request.GET.get('page')
    page_obj= paginator.get_page(page_number)

    return render(request, 'blog/image.html', {'page_obj':page_obj})
    # return page_obj.object_list()
