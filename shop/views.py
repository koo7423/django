from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import shop

from django.contrib import auth

# Create your views here.

def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def login(request):
    response_data = {}
    if request.method =="GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        login_username = request.POST.get('username', None)
        login_password = request.POST.get('password', None)

        if not(login_username and login_password):
            response_data['error']='아이디와 비밀번호를 모두 입력해주세요.'
        else:
            shopuser = shop.objects.get(username=login_username)

            if check_password(login_password, shopuser.password):
                request.session['user'] = shopuser.id
                return redirect('/')
            else:
                response_data['error'] = "비밀번호를 확인해주세요."
        return render(request, 'login.html', response_data)

def  logout(request):
    request.session.pop('user')
    return redirect('/')

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')

    elif request.method =="POST":
        username = request.POST.get['username', None]
        password = request.POST.get['password', None]
        password2 = request.POST.get['password2', None]
        res_data = {}
        if not (username and password and password2):
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != password2:
            res_data['error'] = "비밀번호가 다릅니다."
        else:
            user = shop(username=username, password=make_password(password))
            user.save()
        return render(request, "signup.html", res_data)
