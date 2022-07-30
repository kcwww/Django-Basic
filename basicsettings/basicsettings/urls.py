from django.contrib import admin
from django.urls import path, include
from myapp import views
from accounts import views as accounts_views #include를 이용해 관리하는게 더 좋음 후에 바꿔볼것

#만든 app은 임포트하자.
#include 추가함으로써 url 관리 용이

#미디어 파일 추가 임포트
from django.conf import settings
from django.conf.urls.static import static

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

    path('detail/<int:blog_id>', views.detail, name='detail'), #detail 뒤 숫자가 정수형이고 해당 변수를 선언하여 뒤 views.detail로 변수를 넘겨준다.
    # 127.0.0.1:8000/detail/1
    # 127.0.0.1:8000/detail/2
    # 127.0.0.1:8000/detail/3
    # 127.0.0.1:8000/detail/4

    path('create_comment/<int:blog_id>', views.create_comment, name="create_comment"),

    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup',accounts_views.signup, name="signup"),
    
    path('free',views.freehome, name="freehome"),
    path('freepostcreate',views.freepostcreate, name="freepostcreate"),
    path('freedetail/<int:post_id>',views.freedetail, name="freedetail"),
    path('freenew_create/<int:post_id>',views.new_freecreate, name="new_freecreate"),
    
]

urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# media 파일에 접근할 수 있는 url도 추가해주어야 함