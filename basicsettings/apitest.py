# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys

import json # 파일을 잘 읽기위해서

import urllib.request #url을 사용하기 위한 임포트 pip install requests 해주어야 합니다
from hidekey import SEARCH_MY_API_KEY_ID,SEARCH_MY_API_KEY_SECRET#키 숨기기


client_id = SEARCH_MY_API_KEY_ID
client_secret = SEARCH_MY_API_KEY_SECRET

encText = urllib.parse.quote("태극기") # 검색어
url = "https://openapi.naver.com/v1/search/movie.json?query=" + encText # json 결과로 받아옴 api 요청 링크 영화검색은 query필수 api마다 다름

request = urllib.request.Request(url) # 요청받아온 url을 객체에 저장
request.add_header("X-Naver-Client-Id",client_id) #요청한 객체가 본인이 맞는지 확인하기위해 헤더에 추가
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request) # 클라이언트 아이디와 시크릿을 넣은 객체를 통해 오픈한 내용을 객체에 저장
rescode = response.getcode() #요청한 응답의 코드 저장
if(rescode==200): #200 은 성공 성공시 오픈해서 저장한 객체 읽어 저장
    response_body = response.read()
    #print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode) #실패시 에러코드 출력

resdata = response_body.decode('utf-8') #읽은 데이터를 식별하기 위해 디코딩

#with open('movie.json','w',encoding="UTF-8-sig") as file: #movie.json으로 파일을 작성되어 생성됨
#    file.write(json.dumps(resdata, ensure_ascii=False)) #내용을 파일에 덤프

pydata = json.loads(resdata) #디코딩 한 데이터를 로드
import re #쓸모없는 문자를 지우기 위한 임포트
datas = pydata['items'] #json형식이고 items안에 원하는 데이터들이 있음

for data in datas:  #검색된 내용들 필요없는 문자열을 지우고 출력
    data['title'] = re.sub('<b>|</b>', '', data['title'])
    print(data['title'])

#검색기능
def home(request):
    if(request.method == 'POST'):
        form = SearchForm(request.POST)
        searchword = request.POST.get('search') #search로써 입력한 값을 가져옴
        if(form.is_valid()):
            search_url = 'https://api.themoviedb.org/3/search/movie?api_key='+ my_id +'&language=en-US&query='+ searchword +'&page=1&include_adult=true'
            response = requests.get(search_url)
            resdata = response.text
            obj = json.loads(resdata)
            condata = obj['results']
            newform = SearchForm()
            return render(request,'search.html',{'condata': condata,'searchword':searchword,'form':newform})

    else:
        form = SearchForm()

        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key='+ my_id
        response = requests.get(url)
        resdata = response.text
        obj = json.loads(resdata) #json formatter 를 이용하여 편하기 식별가능함
        condata = obj['results']
        return render(request,'index.html',{'condata' : condata, 'form' : form })