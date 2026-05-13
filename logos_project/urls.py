from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mentoring.urls')), # 메인 페이지를 mentoring 앱으로 연결
]