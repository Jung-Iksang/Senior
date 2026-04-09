# 연습 04: 두 번의 점수를 입력받아 합격 및 불합격 여부를 출력하는 프로그램
# 조건: 평균 70점 이상, 각 점수당 50점 이상 (50점 미만은 과락)

score1 = int(input("1차 점수 입력: "))
score2 = int(input("2차 점수 입력: "))

average = (score1 + score2) / 2

# 평균 70점 이상이고, 각 점수가 50점 이상이면 합격
if average >= 70 and score1 >= 50 and score2 >= 50:
    print("합격")
else:
    print("불합격")
