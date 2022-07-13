from django.db import models
class Blog(models.Model): #이미 있는 장고의 모델클래스 상속
    title = models.CharField(max_length=200) #char형 선언 , 최대글자 200
    body = models.TextField()
    date =  models.DateTimeField(auto_now_add=True)# 현재 시각
    def __str__(self):
        return self.title #타이틀로 표시
    
    #변경사항 추가 후 DB 파일 추가 후 migration 하자



