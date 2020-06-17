from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=20)
#     content = forms.CharField(widget=forms.Textarea)
# forms.Form 사용하니 반복 많음.

# forms.ModelForm 사용하자!
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title form-control',
                'placeholder ': 'Enter the title.',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content form-control',
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
        # fields = ['title', 'content']
        fields = '__all__'
        # exclude = ['title']
   