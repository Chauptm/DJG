from django.shortcuts import render
from .models import products_Form

# Create your views here.

def products(request):
    list= products_Form.objects.all()
    return render(request, 'products/products.html', {'list':list})

def getproducts(request, id):
    listGet= products_Form.objects.get(id= id)
    return render(request, 'products/getproducts.html', {'listGet':listGet})
