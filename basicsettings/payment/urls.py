from django.urls import path
from payment import views

urlpatterns = [
    path('',views.paymentlist),
    path('first',views.paymentfirst),
]