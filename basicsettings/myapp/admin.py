from django.contrib import admin
from .models import Blog #admin사이트에서 해당 db클래스가 제대로 설정이 되었는지

admin.site.register(Blog) #어드민 사이트에 블로그 객체 확인 가능

#admin 계정 만들기는 python manage.py createsuperuser