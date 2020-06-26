from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .models import Post
from django.http import JsonResponse 
# JsonResponse 함수는 Python 딕셔너리를 json으로 바꿔준다.

# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)

@login_required  # login이 안되어 있으면 login 페이지로 redirect 시키는 함수
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')

    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/form.html', context)

@login_required
def like(request, post_pk):
    user = request.user # 로그인 한 사용자
    post = get_object_or_404(Post, pk=post_pk) # 좋아한 포스팅

    # user.like_posts = user가 좋아요 버튼을 누른 게시물들
    # post.like_users = post를 좋아요 한 사람들

    if post in user.like_posts.all(): # 사용자가 좋아요 버튼을 이미 누른경우
        # 좋아요 제거
        user.like_posts.remove(post)
        liked = False
    else: # 좋아요 버튼을 아직 안 누른 경우
        # 좋아요 추가
        user.like_posts.add(post)
        liked = True

    # return redirect('posts:index')

    context = {
        'msg': '좋아요기능이 동작했습니다.',
        'liked': liked,
    }

    return JsonResponse(context)
