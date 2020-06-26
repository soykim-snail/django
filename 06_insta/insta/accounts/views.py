from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model  # User 모델을 안전하게 가져오기 위함
from django.contrib.auth.decorators import login_required



# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('posts:index')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('posts:index')

    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:login')


def profile(request, user_name):    
    User = get_user_model()
    user_profile = get_object_or_404(User, username=user_name)
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, user_pk):
    me = request.user
    you = get_object_or_404(get_user_model(), pk=user_pk)

    # 자기 자신을 팔로우 못하도록 함 (url을 통한 접근을 차단)
    if me == you : # 지금 자기 자신이면
        return redirect('posts:index') # 인덱스로

    if you in me.follow.all(): # 이미 팔로잉 중  # 다음과 정확히 동일함  # if me in you.follower.all():        
        me.follow.remove(you)  # 다음과 정확히 동일함 : # your.follower.remove(me) 
    else:        
        me.follow.add(you)  # 다음과 정확히 동일함 : # your.follower.add(me)
    return redirect('accounts:profile', you.username)