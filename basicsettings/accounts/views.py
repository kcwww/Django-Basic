from django.shortcuts import render, redirect
from django.contrib import auth #특정 개체가 db에 이미 있는지 없는지 판단, 로그인 로그아웃 기능 수행 가능함
# from django.contrib.auth.models import User 이곳에 관리자 계정이나 authenticate 매써드의 user
from myapp import views
def login(request):
    #POST 요청이 들어오면 로그인 처리를 해줌
    if (request.method == 'POST'):
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid,password=pwd) #db에 있는지 없는지 확인해주는 매써드 있다면 user 객체 반환 없으면 none 반환
        if (user is not None):
            auth.login(request, user)
            return redirect(views.home)
        else:
            return render(request, 'login.html')
    #GET 요청이 들어오면 login form을 담고있는 login.html을 띄워주는 역할을 함
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect(views.home)