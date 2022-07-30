from django.db import models
from django.conf import settings
from django.contrib.auth.models import User #유저를 참조하는 객체 임포트
class Blog(models.Model): #이미 있는 장고의 모델클래스 상속
    title = models.CharField(max_length=200) #char형 선언 , 최대글자 200
    body = models.TextField()
    date =  models.DateTimeField(auto_now_add=True)# 현재 시각
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo') #미디어 - blog_photo라는 디렉토리 생성뒤 파일이 추가됨

    def __str__(self):
        return self.title #타이틀로 표시
    
    #변경사항 추가 후 DB 파일 추가 후 migration 하자


#댓글 모델 생성
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey( Blog, on_delete = models.CASCADE ) #on_delete 이 연결되어 있는 객체가 삭제된다면, CASCADE 즉, 같이 삭제된다.
    # 어떤 게시물에 달려있는 댓글인지를 알 수 있는, 댓글이 달린 그 게시물이 쓰임
    def __str__(self):
        return self.comment #댓글로 표시

class FreePost(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)#작성자 참조 user 객체 임포트해야함

    def __str__(self):
        return self.title #타이틀로 표시

class FreeComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(FreePost, null = True, blank = True,on_delete = models.CASCADE)
    author = models.ForeignKey(User,null = True, on_delete=models.CASCADE)#작성자 참조 null = True 는 지금원래 있던 객체들은 기본값을 null 로 한다.
    

    def __str__(self):
        return self.comment #타이틀로 표시