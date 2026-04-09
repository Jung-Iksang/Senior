# 연습 08: MT 장소를 선정하기 위한 프로그램
# MT 장소를 입력받아 딕셔너리에 저장한 후 투표 결과와 최다득표 MT 장소를 출력

# 투표 결과를 저장할 딕셔너리
votes = {}

# 초기 장소들 설정 (0표로 시작)
locations = ["대성리", "춘천", "을왕리", "청평"]
for loc in locations:
    votes[loc] = 0

# 현재 투표 현황 출력
print(" ".join([f"{loc}:{votes[loc]}표" for loc in locations]))

print()
print("<< MT 장소 투표 >>")

# 투표 진행 (빈 문자열 입력시 종료)
while True:
    place = input("장소: ")
    if place == "":
        break

    if place in votes:
        votes[place] += 1
    else:
        votes[place] = 1

# 최종 투표 현황 출력
print(" ".join([f"{loc}:{votes[loc]}표" for loc in locations]))

# 최다득표 장소 찾기
max_votes = max(votes.values())
winner = [loc for loc, v in votes.items() if v == max_votes][0]

print()
print(f"최다득표: {winner} {max_votes}표")
