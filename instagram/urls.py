from . import views
from django.urls import path, re_path, register_converter

# 커스텀 컨버터 만들어 사용하기.


class YearConverter:
    regex = r"20\d{2}"  # 20으로 시작되는 연도만 유효하다.

    def to_python(self, value):  # url로부터 추출한 문자열을 ㅂㅍ에 넘겨주기 전에 변환
        return int(value)

    def to_url(self, value):  # urlreverse 시에 호출
        return str(value)


register_converter(YearConverter, 'year')

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>', views.post_detail),
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>\d+)/', views.archives_year),
    path('archives/<year:year>/', views.archives_year),
    # 윗줄에서 <year:year> 앞의 year는 커스텀 컨버터 이름 이고 뒤의year는 인자
]
