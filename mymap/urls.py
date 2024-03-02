from django.urls import include, path
from . import views

app_name = 'mymap'
urlpatterns = [
    path('', views.index, name='map'),  # '/' 주소에서 index 뷰로 라우팅 (메인 페이지)
    path('members/',views.members,name='members'), 
]