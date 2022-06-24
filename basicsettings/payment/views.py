from django.shortcuts import render

def paymentlist(request):
    return render(request,'payment.html')

def paymentfirst(request):
    return render(request,'paymentfirst.html')