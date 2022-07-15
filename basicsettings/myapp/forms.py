from socket import fromshare
from django import forms #장고에서 폼 임포트
from .models import Blog #내가 만든 객체 임포트

#django 폼
class BlogForm(forms.Form):
    # 내가 입력 받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

# 모델폼
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog #만든 객체 클래스 따옴
        fields = '__all__'  #이건 전부다
        #fields = [ 'title', 'body' ] # 특정 필드만