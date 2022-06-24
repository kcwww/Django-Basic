from django.shortcuts import render

def cartlist(request):
    return render(request,'cart.html')

def cartfirst(request):
    return render(request,'cartfirst.html')   #html 연결 템플릿폴더