from django.http.request import HttpRequest
from django.http.response import HttpResponse
import quickstart
from django.shortcuts import render
from .forms import sp_Form
from .models import sp
from django.views import View
# Create your views here.
class quick(View):
    def get(self, request):
        context= {'sp':sp_Form}
        return render(request, 'quickstart/index.html', context)

    def post(self, request):
        if (request.method=='POST'):
            sp1= sp_Form(request.POST)
            if sp1.is_valid():
                savesp= sp(name= sp1.cleaned_data['name'], logo= sp1.cleaned_data['logo'])
                savesp.save()
                return HttpResponse('Lưu thành công')
        else:
            return HttpResponse('Not Post')
