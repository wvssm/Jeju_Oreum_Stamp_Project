from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
import json, os
from django.core.exceptions import ImproperlyConfigured

secret_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())
    
def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)
    
# Create your views here.
def login_view(request):
    MAP_API_KEY = get_secret('MAP_API_KEY')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None:
            print("인증 성공")
            login(request, user) # 로그인
            response = redirect('map:map')
            response.set_cookie('username', username)
            response.set_cookie('username', username)
            return response
            #data = {
            #    "nick_name" : username,
            #    "MAP_API_KEY" : MAP_API_KEY
            #}
            #return render(request, 'mymap/map.html',data)
        else:
            print("인증 실패")
    return render(request, "users/login.html")