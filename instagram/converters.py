class YearConverter:
    regex = r"20\d{2}"  # 20으로 시작되는 연도만 유효하다.

    def to_python(self, value):  # url로부터 추출한 문자열을 ㅂㅍ에 넘겨주기 전에 변환
        return int(value)

    def to_url(self, value):  # urlreverse 시에 호출
        return str(value)


class MonthConverter(YearConverter):
    regex = r"\d{1,2}"  # 20으로 시작되는 연도만 유효하다.

    # YearConverter를 상속받았기 때문에 아래코드는 필요없음.

    # def to_python(self, value):  # url로부터 추출한 문자열을 ㅂㅍ에 넘겨주기 전에 변환
    #     return int(value)

    # def to_url(self, value):  # urlreverse 시에 호출
    #     return str(value)


class DayConverter(YearConverter):
    regex = r"[0123]\d"
