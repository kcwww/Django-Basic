from django.urls import path
from cart import views #view 임포트

urlpatterns = [
    path('',views.cartlist), #/carts/
    path('first',views.cartfirst), #/carts/first
]

