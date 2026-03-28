from django.contrib import admin
from django.urls import path
from main.views import index  # 우리가 만든 view 가져오기

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'), # 메인 주소로 접속하면 index 함수 실행
]