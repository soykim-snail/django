from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm() ### 
#     context = {
#         'form': form,  ###
#     }
#     return render(request, 'articles/new.html', context)

# decorator 구문을 사용해서, GET과 POST 외에는 405 에러 반환
@require_http_methods(['GET', 'POST'])
def create(request):
    # title = request.POST.get('title')
    # content = request.POST.get('content')    
    # article = Article(title=title, content=content)
    # article.save()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = ArticleForm(request.POST) # 한번에 받고
        # 유효성 검사 (max_length, null, token , ..... 등등)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArticleForm()    
    context = {
        # form 2가지 모습
        # 1. is_valid()에서 통과하지 못한 form ---(에러메세지 포함)
        # 2. else 구문의 form ---(빈 양식)
        'form': form,
    }      
    return render(request, 'articles/create.html', context)



def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid:
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context)


# def delete(request, pk):
#     article = Article.objects.get(pk=pk)
#     if request.method == "POST":
#         article.delete()
#         return redirect('articles:index')
#     return redirect('articles:detail', article.pk)

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')