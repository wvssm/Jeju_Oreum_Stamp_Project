
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls), # 관리자 페이지
    path("mymap/", include('mymap.urls')), # 'myapp' 앱으로 라우팅
    path('login/', include('mymap.urls')),
    path('signup/', include('mymap.urls')),
    path('members/', include('mymap.urls')),
]
