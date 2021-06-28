from django.http.response import HttpResponse
from django.shortcuts import render , redirect
from .forms import registerForm, loginForm
from django.views import View
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class registerUser(View):
    def get(self, request):
        rU= registerForm
        return render(request, 'home/register.html', {'rU': rU})
    
    def post(self, request):
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']

        user= User.objects.create_user(username, email, password)
        user.save()
        return HttpResponse('lưu thành công')

class loginUser(View):
    def get(self, request):
        lU= loginForm
        return render(request, 'home/login.html', {'lU': lU})

    def post(self, request):
        username= request.POST['username']
        password= request.POST['password']
        # cách 1:
        # try:
        #     user = authenticate(request, username= User.objects.get(email= username), password= password)
        # except:

        user = authenticate(request, username= username, password= password)

        if user is not None:
            login(request, user)
            return render(request, 'home/private.html')
        else:
            return HttpResponse('login thất bại')

def logoutUser(request):
    logout(request)
    return redirect('home:loginUser')

class privatePage(LoginRequiredMixin ,View):
    login_url='/login/'

    def get(self, request):
        return render(request, 'home/private.html')

