from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/')
    else:
        user_form = UserCreationForm()
    context = {
        'user_form': user_form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == "POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
			# 검증된 폼에서 유저 객체를 가져오기 위해서는 get_user() 메서드를 사용한다.
            user = login_form.get_user()
			# 로그인 함수를 이용해서 검증된 유저에 대해 "세션"을 생성해준다!
            auth_login(request, user)
            return redirect("/")
    context = {
        'login_form': AuthenticationForm(),
    }
    return render(request, 'accounts/login.html', context)