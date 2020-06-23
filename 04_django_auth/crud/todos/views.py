from django.shortcuts import render, redirect
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

# Create your views here.
@login_required
def index(request):
    form = TodoForm()    
    context = {
        'form': form,
    }
    return render(request, 'todos/index.html', context)


@login_required
def create(request):
    form = TodoForm(request.POST)
    if form.is_valid():
       todo = form.save(commit=False)
       todo.user = request.user
       todo.save()
       return redirect('todos:index')


@login_required
@require_POST
def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')