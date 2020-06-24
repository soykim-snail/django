from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import get_user_model
# get_user_model 은 AUTH_USER_MODEL에 적용시킨 모델 클래스를 찾아옴.

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "phone" )
        # password1 .. 패스워드
        # password2 .. 패스워드 확인