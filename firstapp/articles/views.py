# django import style guides
# 1. standard library
# 2. 3rd party library
# 3. django
# 4. local django

import random
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    foods = ['된장찌게', '햄버거', '스테이크', '김치찌게']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        }
    return render(request, 'dinner.html', context)


def photo(request):    
    url = 'https://picsum.photos/200/300.jpg'
    context = {
        'photo' : url,
    }
    return render(request, 'photo.html', context)

