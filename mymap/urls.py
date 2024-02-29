from django.urls import path
from . import views

app_name = 'map'
urlpatterns = [
    path('', views.index, name='map'),  # '/' 주소에서 index 뷰로 라우팅
    path('about/', views.about, name='about'),  # '/about/' 주소에서 about 뷰로 라우팅
    path('login/',views.login,name='login'), #/app/me 검색하면 나옴
    path('signup/',views.signup,name='signup'), #/app/me 검색하면 나옴
    path('members/',views.members,name='members'), #/app/me 검색하면 나옴
]