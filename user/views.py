from django.shortcuts import render,redirect
from django.views import View
from .models import User

from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Login_screen(View):
    def get(self, request):
        status = request.GET.get('status')
        context = {
            'status':status,
        }
        return render(request, 'login.html', context)
        
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        print(user)
        if user == None :
            return redirect('/user/login/?status=1')
        else:
            login(request, user)
            return redirect('home')

class CreateAccount_screen(View):
    def get(self, request):
        status = request.GET.get('status')
        context = {
            'status':status,
        }
        return render(request, 'create_account.html', context)
    def post(self,request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email)
        db = get_user_model()
        exists = db.objects.filter(email=email)
        print(exists)
        if len(exists)==0:
            print
            db.objects.create_user(username=username, email=email, password=password)
            user = authenticate(request, email=email, password=password) 
            login(request, user)
            return redirect('/?status=9')
        else: 
            return redirect('/user/createAccount/?status=1')

@login_required(login_url='/')
def exit(request):
    logout(request)
    return redirect('home')