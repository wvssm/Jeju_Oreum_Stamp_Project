from django.shortcuts import render
from django.http import HttpResponse
import os
import json
from django.core.exceptions import ImproperlyConfigured
from users.models import User
from .models import Stamp
from .models import Oreum
from django.shortcuts import redirect

secret_file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'secrets.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

     
def index(request):
    if request.method == "POST":
        oname = request.POST.get("oname")
        user_pk = request.user.pk
        stamp = Stamp(oname=oname, author_id=user_pk)
        stamp.save()
        return redirect("mymap:map")
    else:
        MAP_API_KEY = get_secret('MAP_API_KEY')
        user = User.objects.get(username=request.COOKIES.get('username'))
        user_pk = request.user.pk
        stamps = Stamp.objects.filter(author=user_pk).order_by("-created_at") # 최신 게시물이 먼저오도록 정렬
        post_stamp = Stamp.objects.filter(author=user_pk).order_by("-created_at").first()
        oreum = Oreum.objects.get(oname=post_stamp.oname)
        data = {
            'user' : user,
            "MAP_API_KEY" : MAP_API_KEY,
            "stamps" : stamps, # 가져온 게시물들을 posts라는 키로 딕셔너리에 담는다.
            "oreum_data" : oreum
        }
        return render(request, 'mymap/map.html', data)

def members(request):
    return render(request, 'mymap/members.html')
    #return HttpResponse("Welcome to my app!")