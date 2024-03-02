from django.db import models
from django.contrib.auth.models import AbstractUser
# AbstractUser 상속 받기

# Create your models here.
class User(AbstractUser): # AbstractUser 상속하여 유저 클래스 생성
    pass