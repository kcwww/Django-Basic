from django.db import models
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
    post = models.ForeignKey( Blog, on_delete = models.CASCADE )
    # 어떤 게시물에 달려있는 댓글인지를 알 수 있는, 댓글이 달린 그 게시물이 쓰임
    def __str__(self):
        return self.comment #댓글로 표시
