from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import User

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            print("인증 성공")
            login(request, user) # 로그인
            response = redirect('mymap:map')
            response.set_cookie('username', username)
            response.set_cookie('username', username)
            return response
        else:
            print("인증 실패")
    return render(request, "users/login.html")

def logout_view(request):
    logout(request) # 로그아웃 실행
    return redirect("users:login")

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        if User.objects.filter(username=username).exists():
            return redirect("users:signup")
        else:
            user = User.objects.create_user(username,email,password)
            user.save()
            return redirect("users:login")
    return render(request, "users/signup.html")