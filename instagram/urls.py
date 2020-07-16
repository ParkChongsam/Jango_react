from . import views
from django.urls import path, re_path, register_converter
from .converters import YearConverter, MonthConverter, DayConverter

# 커스텀 컨버터 만들어 사용하기.
# class YearConverter:
#     regex = r"20\d{2}"  # 20으로 시작되는 연도만 유효하다.

#     def to_python(self, value):  # url로부터 추출한 문자열을 ㅂㅍ에 넘겨주기 전에 변환
#         return int(value)

#     def to_url(self, value):  # urlreverse 시에 호출
#         return str(value)
# 위 부분을 converters.py로 옮겨서 import해서 사용함.

register_converter(YearConverter, 'year')
register_converter(MonthConverter, 'month')
register_converter(DayConverter, 'day')

app_name = 'instagram'

urlpatterns = [
    path('', views.post_list),
    path('<int:pk>', views.post_detail),
    # path('archives/<int:year>/', views.archives_year),
    # re_path(r'archives/(?P<year>\d+)/', views.archives_year),
    # path('archives/<year:year>/', views.archives_year),
    # 윗줄에서 <year:year> 앞의 year는 커스텀 컨버터 이름 이고 뒤의year는 인자
    path('archive/', views.post_archive, name='post_archive'),
    path('archive/<year:year>/', views.post_archive_year, name='post_archive_year'),
    path('archive/<year:year>/<month:month>',
         views.post_archive_month, name='post_archive_month'),
    path('archive/<year:year>/<month:month>/<day:day>',
         views.post_archive_day, name='post_archive_day'),
]
