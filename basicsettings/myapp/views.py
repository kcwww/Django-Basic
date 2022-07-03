from django.shortcuts import render

def first(request):
    return render(request,'home.html')

def second(request):
    return render(request,'about.html')