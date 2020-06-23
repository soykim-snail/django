from django.shortcuts import render
from .models import Page
from .forms import Form

# Create your views here.
def index(request):
    page = Page.objects.all()
    context = {
        'page' : page,
    }
    return render(request, 'pages/index.html', context)


def create(request):    
    if request.method == 'POST':
        pass
    else:
        pass
    context = {
        'form': Form(),
    }
    return render(request, 'pages/create.html', context)
