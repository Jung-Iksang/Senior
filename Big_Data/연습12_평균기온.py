# 연습 12: 파일(weather.txt)을 읽어서 월의 평균기온을 계산하여 출력하는 프로그램
# 파일에는 월, 최저기온, 최고기온이 저장되어 있음

# 파일 읽기
with open("Big_Data/weather.txt", "r") as f:
    lines = f.readlines()

# 각 줄을 읽어서 평균기온 계산 및 출력
for line in lines:
    data = line.strip().split(", ")
    month = int(data[0])
    min_temp = float(data[1])
    max_temp = float(data[2])

    # 평균기온 계산 (최저 + 최고) / 2
    avg_temp = (min_temp + max_temp) / 2

    print(f"{month}월 평균기온은 {avg_temp:.1f}℃입니다.")