# django import style guides
# 1. standard library
# 2. 3rd party library
# 3. django
# 4. local django

import random
import requests
from pprint import pprint
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')


def dinner(request):
    foods = ['된장찌게', '햄버거', '스테이크', '김치찌게']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        }
    return render(request, 'articles/dinner.html', context)


def photo(request):    
    url = 'https://picsum.photos/200/300.jpg'
    context = {
        'photo' : url,
    }
    return render(request, 'articles/photo.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'articles/hello.html', context)   
    
# 자기소개 페이지 (이름, 나이)
def intro(request, name, age):
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'articles/intro.html', context)

# 곱셈 페이지 (num1, num2)
def gugu(request, num1, num2):
    context = {
        'num1': num1,
        'num2': num2,
        'result' : num1*num2
    }
    return render(request, 'articles/gugu.html', context)

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
    return render(request, 'articles/dtl_practice.html', context)


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
    return render(request, 'articles/word_check.html', context)

# 메아리 만드는 사이트
# 입력을 받는다.
def throw(request):
    return render(request, 'articles/throw.html')

# 입력을 되돌려준다.
def catch(request):
    # pprint(request.META)
    # print(request.GET) # <QueryDict: {'message': ['farfaraway']}>
    # print(request.GET.get('message'))  # farfaraway
    context ={
        'message' : request.GET.get('message'),
        'character' : request.GET.get('character'),
    }
    return render(request, 'articles/catch.html', context)

# 이름 입력을 받는다.
def draw(request):
    return render(request, 'articles/draw.html')

# 로또번호를 뽑아 돌려준다.
def show(request):
    # numbers = random.sample(range(1, 46), 6).sort()  # 리턴값이 none ... 원본을 정렬
    numbers = sorted(random.sample(range(1, 46), 6))  # 리턴값이 있음
    # numbers = random.sample(range(1, 46), 6)
    context = {
        "guest_name": request.GET.get('guest_name'),
        "numbers" : numbers,
    }
    return render(request, 'articles/show.html', context)


def artii(request):
    return render(request, 'articles/artii.html')

def artii_result(request):

    # 1. form에서 넘어온 데이터를 받는다.
    word = request.GET.get('word')

    # 2. ARTII api fontlist로 요청을 보내 폰트 정보를 받는다.
    response = requests.get('http://artii.herokuapp.com/fonts_list').text
    print(response)   
    # 3-d
    # 3x5
    # 5lineoblique
    # 1943____
    # 4x4_offr
    # 64f1____  ... 이하 생략
    print(type(response)) # <class 'str'>

    # 3. 문자열 데이터를 리스트로 변환한다.
    print(response.split('\n'))
    # ['3-d', '3x5', '5lineoblique', '1943____', '4x4_offr', '64f1____', ... 이하 생략
    fonts_list = response.split('\n')

    # 4. 폰트 하나를 랜덤으로 뽑는다.
    font = random.choice(fonts_list)

    # 5. Artii api 주소로 우리가 만든 데이터와 함께 요청을 보낸다.
    ARTI_URL = f'http://artii.herokuapp.com/make?text={word}&font={font}'
    result = requests.get(ARTI_URL).text
    context = {
        'result' : result,
    }
    return render(request, 'articles/artii_result.html', context)

# dorp down 으로 폰트 선택을 추가하자
def artii_drop(request):
    response = requests.get('http://artii.herokuapp.com/fonts_list').text
    # print(response)
    fonts_list = response.split('\n')
    # print(fonts_list)
    context = {
        'fonts_list' : fonts_list,
    }
    return render(request, 'articles/artii_drop.html', context)

def artii_result_drop(request):
    word = request.GET.get('word')
    font = request.GET.get('font')
    ARTI_URL = f'http://artii.herokuapp.com/make?text={word}&font={font}'
    result = requests.get(ARTI_URL).text
    context = {
        'result' : result,
    }
    return render(request, 'articles/artii_result_drop.html', context)