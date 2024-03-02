
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls), # 관리자 페이지
    path('auth/', include("users.urls")), # 'auth'로 라우팅
    path("mymap/", include('mymap.urls')), # 'myapp'으로 라우팅
]
