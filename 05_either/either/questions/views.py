from django.shortcuts import render, redirect, get_object_or_404
from .forms import QuestionForm, AnswerForm
from .models import Question, Answer

# Create your views here.
def index(request):
    return render(request, 'questions/index.html')


def create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('questions:detail', question.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'questions/form.html', context)


def detail(request, question_pk):
    # question = Question.objects.get(pk=question_pk)
    question = get_object_or_404(Question, pk=question_pk)  # 글이 없으면 404 에러 반환하라
    
    answers = question.answer_set.all()
    answer_a = answers.filter(choice='a').count()
    answer_b = len(answers.filter(choice='b'))

    answer_form = AnswerForm()
    context = {
        'question': question,
        'answer_form': answer_form,
        'answer_a': answer_a,
        'answer_b': answer_b,
    }
    return render(request, 'questions/detail.html', context)
    

def answer_create(request, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save(commit=False)
        answer.user = request.user
        answer.question = question
        answer.save()
        return redirect('questions:detail', question_pk)
    