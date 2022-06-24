from django.shortcuts import render

def dashboardlist(request):
    return render(request,'dashboard.html')

def dashboardfirst(request):
    return render(request,'dashboardfirst.html')
