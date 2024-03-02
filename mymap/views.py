from django.shortcuts import render
from django.http import HttpResponse
import os
import json
from django.core.exceptions import ImproperlyConfigured
from users.models import User

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
    MAP_API_KEY = get_secret('MAP_API_KEY')
    user = User.objects.get(username=request.COOKIES.get('username'))
    data = {
        'user':user,
        "MAP_API_KEY" : MAP_API_KEY
    }
    return render(request, 'mymap/map.html', data)

def members(request):
    return render(request, 'mymap/members.html')
    #return HttpResponse("Welcome to my app!")