# Django

version 2.1.15

### 사용방법

- Django 패키지 인스톨

  `$ pip install django==2.1.15`

- 프로젝트 만들기

  `$ django-admin startproject <프로젝트 이름>`

- 어플리케이션 만들기

  `$ python manage.py startapp <앱 이름>`

- 환경 세팅 (settings.py)

  ```python
  INSTALLED_APPS = [ ..로칼앱 추가.., ]
  LANGUAGE_CODE = 'ko-kr'
  TIME_ZONE = 'Asia/Seoul'
  ```

- 서버 켜기

  `$ python manage.py runserver`  ( 서버 끄기 : `ctrl+c` )

- 브라우저에서 로켓 확인하기

- MTV 패턴에 따른 코딩하기

  1. urls.py 작성
  2. views.py 작성
  3. templates 작성

##### 장고 특징:

trailing comma를 허용한다.

### style convention

\# django import style guides

\# 1. standard library

\# 2. 3rd party library

\# 3. django

\# 4. local django

### django template language (dtl)

- variable routing

---

##### 실습: 사용자의 입력값을 그대로 돌려주는 사이트를 만들어 보자

2개의 view가 필요함

1. throw : 사용자로부터 입력을 받아 서버로 보내는 view
2. catch : 입력받은 값을 보여주는 view

---

# http request method

1. GET
   - HTTP method 중 GET 요청은 서버로부터 정보를 조회하는데 사용됩니다.
   - 서버의 데이터나 상태를 변경시키지 않기 때문에 단순 조회(html)할 때 사용한다.
   - 데이터를 전송할 때 http body가 아니라 쿼리스트링을 통해 전송된다. 

#### form에서 중요한 것

1. 데이터를 어디로 보낼지 => action
2. 어떤 방식으로 보낼지 => method
3. 어떤 데이터를 보낼지 => input type
4. 데이터의 이름은 어떻게 붙일지 => name
5. 제출 => submit

#### Django Template Language (DTL)

- variable 사용 : `{{ variable }}`

- 반복문, 조건문, 반복조건, 필터 등등

  ```django
  {% for ... in ... %} 
  {% empty %}
  {% endfor %}
  ```

---

### 프로젝트 만들기 (FIRSTAPP)

#### 관리를 위해서 다음을 적용

1. URL 로직 분리

   - 두번째 app을 생성할 때….. 하나의 urls.py에서 모든 문서 path를 관리하기 어려워짐.
   - 프로젝트의 urls를 각 앱으로 분리하자.
   - 기존 url 이 바뀌어버려서 지금까지 작업한 모든 url을 바꿔줘야 함
   - 그건 어려우니 그냥 url에 이름을 붙이자.

2. URL Name : 

   - `{% urls “<url 이름>” %}`
   - 그런데,,, 두개의 앱에서 url 이름이 같다면?
   - 어떤 앱의 url 이름인지 app_name을 설정하자.

3. URL Namespace : 

   `{% urls "app-name:view-name" v1 v2 %}`

4. Django Namespace : 

   장고는 templates를 한곳에 모아두므로 템플릿 파일명이 곂치면 우선순위에 따라 인식한다. 그래서 templates/<앱이름>으로 강제로 경로를 추가한다.

   INSTALLS_APP 에 등록한 순서대로 인식

   > app_name/
   >
   > ​	templates/
   >
   > ​		**app_name/**
   >
   > ​			index.html
   >
   > ​			hello.html

5. Django Template Inheritance 적용:

   - 템플릿의 재사용성을 위해 상속을 사용했다.

     프로젝트에 기본 html을 만들고, 나머지는 이것을 상속한다.

     ```django
     {% extents 'base.html' %}
     {% block <블록이름> %}내용 오버라이드{% endblock %}
     ```

     그런데,,

   장고는 기본적으로 template을 app-name/templates 에서 찾는다.  setting에 추가하여 firstapps/templates도 찾을 수 있게 하자.

   ```django
   TEMPLATES = ... 생략 ...   
           'DIRS': [os.path.join(BASE_DIR, 'firstapp', 'templates')],
   ```

6. static

   장고는 기본적으로 static을 app-name/static 에서 찾는다. setting에 추가하여 firstapps/static도 찾을 수 있게 하자.

   (사용방법은 공식문서를 사용하자.) https://docs.djangoproject.com/en/2.1/howto/static-files/ 

   ```django
   STATICFILES_DIRS = [
       os.path.join(BASE_DIR, 'firstapp', 'static'),
   ]
   ```

   





## VScode, markdown 꿀팁

polar code로 사진찍기, github issue에 사진 저장하고 url 받기

단축키들 : `alt + 화살표` , `cntrl + l` 

콘솔 단축키 : `cntrl + l` (화면 지우기)



---

# ORM (Object Relational Mapping)

- OOP 프로그래밍에서 RDBMS를 연동할 때, 데이터베이스와 OOP 프로그래밍 언어간에 호환되지 않는 데이터를 변환하는 프로그래밍 기법

![image](https://user-images.githubusercontent.com/58576911/84608322-deb2dc00-aeec-11ea-82e4-e32a132245a6.png)

## 장점

- SQL을 몰라도 코딩 가능함. 생산성 좋다

## 단점

- 완벽하게 대체는 불가능

---

# Python 클래스

### 클래스

- 클래스란 객체를 표현하기 위한 문법.

### 인스턴스

- 메모리상에 할당된다.
- 고유의 속성(attribute)를 가지며 클래스에서 정의한 행위(behavior)를 수행할 수 있다. 
- 인스턴스의 행위는 클래스에 정의된 행위에 대한 메서드를 공유함으로써 메모리를 절약할 수 있음

### 속성(attribute)

- 클래스/인스턴스가 가지고 있는 속성(값)

### 메서드(method)

- 클래스/인스턴스가 할 수 있는 행위(함수)

### self

- 인스턴스 자기자신. 
- 메소드 정의할 때 반드시 첫번째 인자는 self

---

### Django Models

1. `CharField()`

   - 길이의 제한이 있는 문자열을 만들 때
   - 

2. `TextField()`

   - 길이의 제한이 없는 문자열을 만들 때

3. `DateTimeField()`

   `models.dateTimeField( … …. )`

   `auto_now_add = True`

   `auto_now = True`

---

# Model 작성 3단계

1. models.py 작성

   models.py 에 원하는 데이터 스키마를 클래스로 작성한다.	

```python
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 데이터베이스의 최초 생성일
    updated_at = models.DateTimeField(auto_now=True) # 데이터 최신 수정일
```



2. migrations (설계도 작성)

   설계도를 작성한다.

```
$ python manage.py makemigrations
```

​		migrations이 ORM에 의해서 어떻게 sql 문으로 해석되어 동작할 지 미리 확인할 수 있다.

```
$ python manage.py sqlmigrate <앱이름> <마이그레이션 넘버>
```



3. migrate (DB 작성 및 구축)

```
$ python manage.py migrate
```



python 콘솔 사용하기

- ipython 인스톨 하고 `pip install ipython`, `ipython` 실행하자.

- 장고에서 ipython을 실행하자 ..

  ```python
  python manage.py shell
  ```

  

---

## objects

- models.py에 작성한 클래스를 불러와서 사용할 때 DB와의 인터페이스 역할을 하는 매니저

## Query Set

- objects 매니저를 사용하여 복수의 데이터를 가져오는 함수를 사용할 때 반환되는 객체 타입
- 단일 객체는 **Query** (class의 인스턴스로 반환)
- query를 DB에게 보내서 CRUD 한다. 

---

# Django ORM 문법

## CREATE

```python
# 1
article = Article()
article.title = 'first'
article.content = 'django!'
article.save()

# 2
article = Article(title='second', content='django')
article.save()

# 3
Article.objects.create(title='third', contend='django!')
```

## READ

```python
# 모든 객체 조회
Article.objects.all()

# 특정 객체 조회
Article.objects.get(pk=1)

# 특정 조건 객체 가져오기
Article.objects.filter(title='first')
Article.objects.filter(title='first', content='django!')

# 내림차순
Article.objects.order_by('-pk')

# LIKE (FIELD LOOKUPS)
Article.objects.filter(title__contains='fi')   
Article.objects.filter(title__startswith='fi')
Article.objects.filter(content__endswith='!')
```

- `.get()`을 사용할 때 해당 객체가 없으면 `DoesNotExist` 에러가 발생하고, 여러 개일 때 `MultipleObjectReturned` 에러가 발생함. ==> 이와 같은 특징 때문에 **pk** 사용한다.
- 읽어온 결과는 `Article` 객체 또는  `QuerySet` 로 저장된다. 

```shell
# Article 객체
In [8]: Article.objects.get(pk=2)
Out[8]: <Article: Article object (2)>

# QuerySet
In [9]: Article.objects.filter(my_title__startswith="tt", my_content__endswith="d")
Out[9]: <QuerySet [<Article: Article object (1)>, <Article: Article object (2)>]>
```



## UPDATE

```python
article = Article.objects.get(pk=1) # 선택하고
article.title = 'edit title' # 업데이트 한 후
article.save() # 저장
```

## DELETE

```python
article = Article.objects.get(pk=1) # 선택하고
article.delete() # 삭제
```

---

# 관리자 기능 사용하기

계정 또한 데이터이기 때문에 반드시 migrate 작업 후에 관리자 계정을 생성해야 한다.

## admin 작성 순서

1. `python manage.py createsuperuser`

2. `admin.py` 작성

   ```python
   # Register your models here.
   Class ArticleAdmin(admin.ModelAdmin):
       list_display = ['pk', 'title', 'content', 'created_at',]
       list_editable = ['title']
   admin.site.register(Article, ArticleAdmin)
   ```

   

---

# CRUD 웹사이트



## CREATE

- 필요한 view 함수는 2개
- new 와 create 만들자

### POST

​	*Why POST?*

- 사용자는 djangto게 ‘html 파일 줘!’ (GET) 가 아니라 ‘~한 레코드를 생성해 줘! (POST)’ 를 원하기 때문에 **http method POST**를 사용해야 한다.
- 데이터는 URL에 직접 노출되어서는 안된다. (query의 형태를 통해 db구조 (schema)가 유추될 수 있어서 보안에 취약함)
- DB를 조작할 때는 GET 이 아닌 POST 를 쓴다. 중요한 요청이기 때문에 신원확인 필요하기 때문임.

### 1. CSRF (Cross-site request forgery) 처리

- Django는 기본적으로 CSRF 공격을 대비하기 위한 보안세팅이 되어있음 (`setting.py`)

  ```python
  MIDDLEWARE = [    ...,
      'django.middleware.csrf.CsrfViewMiddleware', # Cross-site request forgery 검증               
  ]
  ```

- 그래서 POST로 그냥 정보를 넘기면 403 Forbidden 에러가 뜬다.

- 이것을 방지하기 위해 POST 전송할 때 csrf-token을 함께 넘겨주자.

  ```django
  <form .... method="POST"> ... 
  	{% csrf_token %}    
  </form>
  ```

- 브라우저에서 암호화 된 token 값이 넘어오는 것을 확인할 수 있다.

  ```html
  <input type="hidden" name="csrfmiddlewaretoken" value="tpVpOEtvaDiZ0vugVcmCz5SUBVSeE3lBmfTTO2wp6kzDkKUmYxrWSC6d4rFCbFRN">
  ```

### 2. redirect

- 저장 작업이 끝난 후 원하는 페이지로 `redirect` 해준다.

  ```python
  from django.shortcuts import render, redirect # redirect 임포트
  def ....(...):
      return redirect('articles:index') # 리턴 리다이렉트
  ```

- 필요한 argument 값을 함께 전달할 수도 있다.

  ```python
  def ....(...):
      article = Article(... ...)
      return redirect('articles:detail', article.pk) # pk 값을 함께 전달
  ```

## READ

- ```
  Article.objects.all()
  ```

  

## UPDATE

- edit 과 update 만든다.

## DELETE

- POST 방식으로만 작동하도록 조작하자.

  템플릿에 `<a>` 대신에 `<form>`을 쓰자. (POST method에서는 csrf_token 도 잊지 말자.)

  ```django
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
      {% csrf_token %}
      <button>삭제</button>
  </form>
  ```

  view 함수가 POST 에서만 db 수정하도록 분기하자.

  ```python
  def delete(request, pk):
      ......
      if request.method =='POST'
      	article.delete()
      	return ...
      else:
          return ...
  ```

---

# Django form

참고자료 : 	

> [폼과 함께 작업하기] https://docs.djangoproject.com/ko/2.1/ref/forms/fields/	
>
> [Form fields] https://docs.djangoproject.com/ko/2.1/topics/forms/  
>
> [Widgets] https://docs.djangoproject.com/en/3.0/ref/forms/widgets/

- form 내 field 들, field 배치, widget, label … 유효한 값 등을 정의하고 비유요한 field에 관련된 에러메세지를 결정한다.

- 유효성 체크 : 우리가 직접 form 태그를 작성하는 것보다 유효한 데이터에 요구되는 여러 동작을 올바륵 하기 위해서 제공하는 기능

  

- 장고 템플릿 표현

  `<p>` ,` <ul>` , `<table>` 태그로 감싸기 옵션이 가능

  ```django
  {{ form }}
  {{ form.as_p }}
  {{ form.as_ul }}
  {{ form.as_table }}
  ```

- `forms.py` 만들기

  - `ModelForm`
    - django가 해당하는 모델에서 양식에 필요한 정보를 이미 정의했다.

  ```python
  from django import forms
  from .models import Article
  
  # ArticleForm 사용하면... 반복작업 많으니
  class ArticleForm(forms.Form):
      title = forms.CharField(max_length=20)
      content = forms.CharField(widget=forms.Textarea)
  
  # ModelForm 사용하자!
  class ArticleForm(forms.ModelForm):
      title = forms.CharField(
          label='제목',
          widget=forms.TextInput(
              attrs={
                  'class': 'my-title',
                  'placeholder ': 'Enter the title.',
              }
          )
      )
      content = forms.CharField(
          label='내용',
          widget=forms.Textarea(
              attrs={
                  'class': 'my-content',
                  'placeholder': 'Enter the content.',
                  'cols' : 30,
                  'rows' : 10,
              }
          )
      )
      # ArticleForm 클래스에 대한 정보를 작성하는 곳 (장고 문법)
      class Meta:
          # 참조할 모델을 선택한다.        
          model = Article
          # 사용한 필드를 선택한다.
          fields = ['title', 'content']  # fields = '__all__'  # exclude = ['title']
  ```

- url 합치기

  - 작성하기(new)와 저장하기(create)를 하나로 합치자. 요청이 GET으로 오면 new 역할, POST로 오면 create 역할.
  - 수정하기(edit)와 저장하기(update)도 하나로 합치자. 요청이 GET으로 오면 edit 역할, POST로 오면 update 역할

  ```python
  urlpatterns = [
      ...
      path('create/', views.create, name=create),
      path('<int:pk>/update/', views.update, name=update),
  ]
  ```

- view 합치기

  - CREATE : 요청이 GET으로 오면 new 역할, POST로 오면 create 역할.

    ```python
    def create(request):
        if request.method == "POST":
            form = ArticleForm(request.POST)
            if form.is_valid():
                article = form.save()
    	        return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)
    ```

  - UPDATE : 요청이 GET으로 오면 edit 역할, POST로 오면 update 역할

    ```python
    def update(request, pk):
        if request.method == "POST":
            article = Article.objects.get(pk=pk)
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
        context = {
            'form': form,
        }
        return render(request, 'articles/update.html', context)
    ```

### Form에 Bootstrap4 적용하기

- class 이용하는 방법
- library 이용하는 방법

## decorator

```python
from django.views.decorators.http import require_http_methods
@require_http_methods(["GET", "POST"])
def ...(...):
```



---

# Django many to one (복수 모델 사용하기)

관계설정이란? 여러개의 테이블을 만들고, 칼럼이나 새 테이블로 관계를 설정해 준다.

- shell 사용하여 콘솔에서 ORM 사용하기

settings.py설정 

```python
INSTALLED_APPS = [
    ...
  'django_extensions', # 추가하였음……
	...		
]
```

shell 창에서

```
$ python manage.py shell_plus
```

글을 작성하고, 조회하자

```
In [1]: Article.objects.all()
Out[1]: <QuerySet []>

In [2]: Article.objects.create(title="Hello", content="hihi!")
Out[2]: <Article: Article object (1)>


```

---

# File 전송하기

* `<form>` 안에  `enctype="multipart/form-data"` 설정해야 함

  * application/x-www-form-urlencodedㄷㄷ치
    * Default. All characters are encoded before sent (spaces are converted to "+" symbols, and special characters are converted to ASCII HEX values)
  * multipart/form-data
    * No characters are encoded. This value is required when you are using forms that have a file upload control
  * text/plain
    * Spaces are converted to "+" symbols, but no special characters are encoded

* 미디어 파일이 저장될 위치를 설정함

  `settings.py`

---

# n : n 연관

1:N 연관이 양쪽에서 생기는 경우 의미함.

(예시:  게시글의 좋아요, 팔로우와 팔로워, 환자와 의사, … )

model을 작성할 때 `models.ManyToManyField` 으로 연결을 지정한다. (이전에 연결이 존재하여 이름이 충돌한다면, `related_name=` 으로 이름수정 가능함.) 

ManyToMany 연결을 위해서, 장고 내부적으로는 매칭테이블이 만들어진다.

| #    | id   | post_id | user_id |
| ---- | ---- | ------- | ------- |
| 1    | 4    | 5       | 2       |
| 2    | 5    | 4       | 2       |
| 3    | 11   | 1       | 2       |
| 4    | 12   | 7       | 2       |

---

# RESTFul

![img](https://gmlwjd9405.github.io/images/network/rest.png)

“Representational State Transfer” 의 약자
자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다.
https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html



REST API 란?

“Representational State Transfer” 의 약자
자원을 이름(자원의 표현)으로 구분하여 해당 자원의 상태(정보)를 주고 받는 모든 것을 의미한다.
https://gmlwjd9405.github.io/2018/09/21/rest-and-restful.html

---

# ORM 작동의 3단계

### 1) `models.py`  : 파이썬의 클래스 모델링

### 2) `makemigrations` : RDB  CRUD를 위한 번역

### 3) `migrate` : db.sqlite3 만들기

---

# onclick event 설정

JS 이벤트 설정의 키 포인트

1) 누구를

```javascript
var ... = document.querySelectorAll('...')
```

2) 어떻게 했을 때         

`click`, `...`

3) 뭐뭐를 한다.

```javascript
likeButton.addEventListener('click', function(){...})
누구를.addEventListenr('어떻게', function(){뭐뭐...})
```

(참고) `things.forEach(익명함수)` :  for thing in things function(){ … …}



---

상대경로와 절대경로

`/` : 최상단 루트 경로부터 시작함을 의미함.

---

## Django Pagination

페이징 요청은 이런식

localhost:8000/articles?page=3



- django pagination 공식 문서에서 샘플코드 따오기

```python
from django.shortcuts import render
from myapp.models import Contact

def listing(request):
    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    # 사용자가 보낸 요청에 page 라는 요청이 있으면 가져와라 
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})
```

- 데이터가 여러개인 상황에서 ,  쿼리의 결과값으로 리턴된 리소스를 분할하여 전달 하는 것을 의미 . 즉 . 페이징

수업자료에서 세팅

1.  07_map  pull  해오기
2.  migrate 하고 runserver
3.  <views.py>- articles 에서 Paginator  import  하기 

```
from django.core.paginator import Paginator
```

4. <views.py>- articles 에서 index에 pagination 하는 구문 추가 작성하기

(참고) Django bootstrap pagination …. 사용하면 편리

-----

## django fixture

### dumpdata

```python
django-admin dumpdata [app_label[.ModelName] [app_label[.ModelName] ...]]
# 다시 말하면 콘솔창에 다음과 같이 입력하자
$ python manage.py dumpdata articles.Article
# 이것을 파일에 저장
$ python manage.py dumpdata articles.Article > articles.json
# 들여쓰기 옵션
$ python manage.py dumpdata --indent=2 articles.Article > articles.json
```

### loaddata

자료는 app 폴더의 `fixtures` 안에 있어야 함.