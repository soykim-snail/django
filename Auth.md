# Auth

authorization : 권한의 부여

authentication : 인증

---

프로젝트와 앱 생성하기

```
$ django-admin startproject crud
$ cd crud
$ python manage.py startapp accounts
$ python manage.py startapp todos
```

앱등록  : *settings.py*

```python
INSTALLED_APPS = [
    'accounts',
    'todos',
```

base template 만들기  (crud > templates > base.html)

템플릿 등록: *settings.py*

```python
TEMPLATES = [
...
        'DIRS': [os.path.join(BASE_DIR, 'crud', 'templates')],
```

auth 관련 기본 테이블들을 활성화

```
$ python manage.py migrate
```



## signup

## login

## logout



패스워드는 **sha256** 해싱처리되어 보관된다.

- sha256 : 단방향 암호화
- salt  : 패스워드에 임의의 문자열을 추가함
- iteration : 18만번 반복 수행

> Password: **algorithm**: pbkdf2_sha256 **iterations**: 180000 **salt**: lnKZiY****** **hash**: uVTbyV**************************************

기본 창은 다음과 같다.

![image](https://user-images.githubusercontent.com/58576911/85348670-42fe1d00-b537-11ea-8fa7-fbc1930f4530.png)

i18n (internationalization) 에 따라서 언어 표현이 된다.



> ### How to log a user in[¶](https://docs.djangoproject.com/en/3.0/topics/auth/default/#how-to-log-a-user-in)
>
> If you have an authenticated user you want to attach to the current session - this is done with a [`login()`](https://docs.djangoproject.com/en/3.0/topics/auth/default/#django.contrib.auth.login) function.

login 기능 넣기 : *views.py*

```python
# 로그인에 필요한 빌트인 Form을 임포트하고,
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# 빌트인 login 함수
from django.contrib.auth import login as auth_login

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)
```



![image](https://user-images.githubusercontent.com/58576911/85353041-4f3ba780-b542-11ea-816d-80d027a794bb.png)

---

model 만들기

```python
user = models.models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```





로그인 한 경우만 사용할 수 있도로 하려면, `@login_required` 데코레이터를 사용한다. (`from django.contrib.auth.decorators import login_required` 임포트 필요함)

