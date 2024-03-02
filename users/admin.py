from django.contrib import admin
from .models import User
# Register your models here.

admin.site.register(User) # 관리자 페이지에 User 모델 등록
