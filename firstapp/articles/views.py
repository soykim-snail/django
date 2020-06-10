# django import style guides
# 1. standard library
# 2. 3rd party library
# 3. django
# 4. local django

import random
from datetime import datetime
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


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)   
    
# 자기소개 페이지 (이름, 나이)
def intro(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'intro.html', context)

# 곱셈 페이지 (num1, num2)
def gugu(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'result' : num1*num2
    }
    return render(request, 'gugu.html', context)

# dtl 학습
def dtl_practice(request):
    foods = ['짜장면', '초밥', '차돌짬뽕', '콩국수']
    empty_list = []
    messages = 'Life is short, python is long.'
    datetime_now = datetime.now()
    words = ['장발장', '신숙주', '토마토', '기러기']
    context = {
        'foods' : foods,
        'empty_list': empty_list,
        'messages': messages,
        'datetime_now': datetime_now
    }
    return render(request, 'dtl_practice.html', context)


# 회문 (palindrome) 체크
def word_check(request, word):
    # 단어를 회문인지 체크    
    if word == word[::-1]:
        pal = True
    else:
        pal = False
    context = {
        'word' : word,
        'pal' : pal,
    }
    return render(request, 'word_check.html', context)