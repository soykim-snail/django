from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
# 전체 글 보기
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 게시글 입력용 화면
def new(request):
    return render(request, 'articles/new.html')

# 게시글 저장
def create(request):
    # 1. new 에서 보낸 데이터 받기
    title = request.POST.get('title')
    content = request.POST.get('content')

    # 2. db에 저장하기
    # # 방법1 : 인스턴스 생성하고 세팅
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # # 방법2 : 세팅값 주면서 인스턴스 생성
    article = Article(title=title, content=content)
    article.save()

    # # 방법3 : 인스턴스 생성 메소드 사용 --- 데이터 유효성 검사 타이밍이 없다.
    # Article.objects.create(title=title, content=content)    
    # return redirect('articles:index') # 요청을 index로 보낸다.
    return redirect('articles:detail', article.pk) # 요청을 detail로 보낸다. (pk를 함께 보내준다.)

# pk로 게시글 조회
def detail(request, pk):
    article = Article.objects.get(pk=pk) # 글을 찾고
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

# DELETE
def delete(request, pk):
    print(request.method)
    article = Article.objects.get(pk=pk)
    # POST 일 때 만 동작하도록 분기
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', pk)

# 수정하는 화면
def edit(request, pk):
    article = Article.objects.get(pk=pk) # 특정하고
    context = {
        'article': article,
    }
    return render(request, 'articles/edit.html', context)

# UPDATE 실행
def update(request, pk):
    # 1. 수정할 게시글 조회
    article = Article.objects.get(pk=pk) # 특정하고
    # 2. edit에서 보낸 데이터를 받아서 기존 값을 업데이트
    article.title = request.POST.get('title')  # 내용 변경
    article.content = request.POST.get('content') # 내용 변경
    article.save()    # 저장
    return redirect('articles:detail', pk)