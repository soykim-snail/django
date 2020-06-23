from django.shortcuts import render, redirect
from .models import Page

# Create your views here.
def index(request):
    pages = Page.objects.all()
    context = {
        'pages': pages,
    }
    return render(request, 'pages/index.html', context)


def new(request):
    return render(request, 'pages/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    page = Page(title=title, content=content)
    page.save()
    return redirect('pages:index')


def detail(request, pk):
    page = Page.objects.get(pk=pk)
    context = {
        'page': page,
    }
    return render(request, 'pages/detail.html', context)


def edit(request, pk):
    page = Page.objects.get(pk=pk)
    context = {
        'page' : page,
    }
    return render(request, 'pages/edit.html', context)

def update(request, pk):
    page = Page.objects.get(pk=pk)    
    page.title = request.POST.get('title')
    page.content = request.POST.get('content')
    # print(request.POST.get('title'), request.POST.get('content'))
    page.save()
    return redirect('pages:detail', pk)



def delete(request, pk):
    page = Page.objects.get(pk=pk)
    if request.method == 'POST':
        page.delete()
        return redirect('pages:index')
    else:
        return redirect('pages:detail', pk)

