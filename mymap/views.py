from django.shortcuts import render
from django.http import HttpResponse
import os
import json
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
    
def index(request):
    #return render(request, 'mymap/map.html')
    #return HttpResponse("Welcome to my app!")
    MAP_API_KEY = get_secret('MAP_API_KEY')

    if request.method == 'POST':
        nick_name = request.POST.get('id')
        request.session['id'] = nick_name

        #nick_name = request.POST.get('id')
        data = {
            "nick_name" : nick_name,
            "MAP_API_KEY" : MAP_API_KEY
        }

        return render(request,'mymap/map.html',data)
    
    else: 
        nick_name = request.session.get('id', '사용자') # 
        data = {
            
            "nick_name" : nick_name,
            "MAP_API_KEY" : MAP_API_KEY
        }
        return render(request, 'mymap/map.html',data)
        

def about(request):
    return HttpResponse("About page")

def login(request):
    return render(request, 'mymap/login.html')

def signup(request):
    return render(request, 'mymap/signup.html')

def members(request):
    return render(request, 'mymap/members.html')
    #return HttpResponse("Welcome to my app!")