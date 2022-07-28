from socket import fromshare
from django import forms #장고에서 폼 임포트
from .models import Blog, Comment #내가 만든 객체 임포트

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
    
    def __init__(self, *args, **kwargs): #클래스를 사용하기 위한 폼
        super(BlogModelForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "내용을 입력해주세요",
            'rows': 20,
            'cols' : 100
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment #만든 객체 클래스 따옴
        fields = ['comment']  #이것만 입력받음

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }
