# 연습 03: 월을 입력받아 계절을 출력하는 프로그램
# 3~5월은 봄, 6~8월은 여름, 9~11월은 가을, 12~2월은 겨울

month = int(input("월 입력: "))

if 3 <= month <= 5:
    season = "봄"
elif 6 <= month <= 8:
    season = "여름"
elif 9 <= month <= 11:
    season = "가을"
elif month == 12 or 1 <= month <= 2:
    season = "겨울"
else:
    season = "잘못된 입력"

print(f"{month}월은 {season}")
