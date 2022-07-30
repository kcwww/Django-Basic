from django.shortcuts import render, redirect, get_object_or_404 # 리다이렉트, pk값을 이용해 특정모델 객체 하나만 가져옴
from .models import Blog #내가 만든 객체 임포트
from django.utils import timezone #자주 사용 임포트
from .forms import BlogForm, BlogModelForm, CommentForm # django form, modelform



#html 이동 함수
def first(request):
    return render(request,'home.html')

def second(request):
    return render(request,'about.html')


#글 작성 GET POST 함수

def home(request):
    #블로그 글들을 모조리 띄우는 코드
    #posts = Blog.objects.all() #  블로그 객체들 모조리 가져옴
    posts = Blog.objects.filter().order_by('-date') #정렬해서 가져옴, 날짜를 기준으로 가져와서 정렬 내림차순 최신글
    return render(request,'index.html',{'posts':posts})

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request,'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'): #메써드가 post요청을 받았을때
        post = Blog() #객체 생성
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect(home) #리다이렉트 홈페이지

# django form을 이용해서 입력값을 받는 함수
#GET 요청과 ( = 입력값을 받을 수 있는 html을 갖다 줘야 함)
#POST 요청 ( = 입력한 내용을 DB에 저장. form에서 입력한 내용을 처리 )
#둘 다 처리가 가능한 함수
def formcreate(request):
    #입력된 데이터 저장
    if (request.method == 'POST'):
        form = BlogForm(request.POST)
        if (form.is_valid()): #유효성 검사
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect(home)
        #입력 내용을 DB에 저장 #is_valid는 유효값 검사 charfield 등 cleaned_data는 검사후 데이터
    else:
        form = BlogForm()
        #render()의 세번째 인자로 views.py 내의 데이터를 html에 넘겨줄 수 있다. 단, 딕셔너리 자료형
    return render(request,'form_create.html',{'form':form}) 

# django modelform을 이용해서 입력값을 받는다. 모델폼에 이미 객체가 있어 따로 객체를 선언하지 않아도 됨
def modelformcreate(request):
#입력된 데이터 저장
    if (request.method == 'POST' or request.method == 'FILES'):
        form = BlogModelForm(request.POST, request.FILES)
        if (form.is_valid()):
            form.save() #modelform 같은 경우는 위와 다르게 save 매써드가 이미 존재하여 form.save()가 가능함
            return redirect(home)
        #입력 내용을 DB에 저장 #is_valid는 유효값 검사 charfield 등 cleaned_data는 검사후 데이터
    else:
        form = BlogModelForm()
        #render()의 세번째 인자로 views.py 내의 데이터를 html에 넘겨줄 수 있다. 단, 딕셔너리 자료형
    return render(request,'form_create.html',{'form':form}) 

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 데이터 베이스로부터 가지고옴
    # blog_id 번째 블로그 글을 detail.html로 띄워주는 코드
    # 인자를 2개 받아야함
    blog_detail = get_object_or_404(Blog, pk=blog_id) #pk값이 id인 객체를 가져옴
    
    comment_form = CommentForm()
    
    return render(request, 'detail.html',{'blog_detail':blog_detail,'comment_form':comment_form}) #댓글 보여주기
    
def create_comment(request,blog_id):
    filled_form = CommentForm(request.POST)

    if (filled_form.is_valid()):
        finished_form = filled_form.save(commit=False) #저장되기전 상태
        finished_form.post = get_object_or_404( Blog, pk=blog_id ) #pk값이 id인 객체를 가져와서 댓글에 post에 넣음
        finished_form.save() # 저장
    
    return redirect( detail, blog_id )

####################################################################

def freehome(request):
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request,'free_index.html',{'freeposts':freeposts})

def freepostcreate(request):
    #request method가 POST일 경우
        # 입력값 저장
    if (request.method == 'POST' or request.method == 'FILES'):
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user
            unfinished.save()
            return redirect('freehome')
    #request method가 GET일 경우
        #form 입력 html 띄우기
    else:
        form = FreePostForm()
        return render(request, 'free_post_form.html', {'form':form})

def freedetail(request,post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    
    return render(request,'free_detail.html',{'post_detail':post_detail,'comment_form':comment_form})

#댓글 저장
def new_freecreate(request,post_id):
    #request method가 POST일 경우
        # 입력값 저장
    if (request.method == 'POST'):
        filled_form = FreeCommentForm(request.POST)
        if (filled_form.is_valid()):
            finished_form = filled_form.save(commit=False)
            finished_form.author = request.user
            finished_form.post = get_object_or_404(FreePost,pk=post_id)
            finished_form.save()
            return redirect('freedetail',post_id)