from django.contrib import admin
from django.urls import path, include
from myapp import views

#만든 app은 임포트하자.
#include 추가함으로써 url 관리 용이

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first),

    path('second/',views.second), #직접 만든 앱 함수구현

    path('carts/', include('cart.urls')), #include를 통해 해당 하위 url들 관리 용이
    path('dashboards/',include('dashboard.urls')),
    path('payments/',include('payment.urls')),

    # html form을 이용해 블로그 객체 만들기
    path('new/',views.new, name='new'), #name 스페이스는 html에서 중괄호 퍼센트 url 'name' 퍼센트 중괄호 // 이걸 연결
    path('create/',views.create, name='create'),

    # django form을 이용해 블로그 객체 만들기 #forms.py 만들어야함
    path('formcreate/',views.formcreate, name='formcreate'),

     # django modelform을 이용해 블로그 객체 만들기 #forms.py 만들어야함
    path('modelformcreate/',views.modelformcreate, name='modelformcreate'),

]

#http://127.0.0.1:8000/