# # ===== Python 입출력 예제 =====

# # 1. 기본 출력 (print)
# print("Hello, World!")
# print(123)
# print(3.14)

# # 2. 여러 값 출력
# print("이름:", "홍길동", "나이:", 20)

# # 3. sep - 구분자 변경
# print("A", "B", "C", sep="-")      # A-B-C
# print("2026", "03", "18", sep="/") # 2026/03/18

# # 4. end - 줄바꿈 변경
# print("Hello", end=" ")
# print("World")  # Hello World (같은 줄)

# # 5. f-string (포맷 문자열)
# name = "홍길동"
# age = 20
# print(f"이름: {name}, 나이: {age}")

# # 6. format() 메서드
# print("이름: {}, 나이: {}".format(name, age))
# print("이름: {0}, 나이: {1}".format(name, age))

# # 7. % 포맷팅 (구버전)
# print("이름: %s, 나이: %d" % (name, age))

# # 8. 숫자 포맷팅
# pi = 3.141592
# print(f"소수점 2자리: {pi:.2f}")  # 3.14
# print(f"5자리 확보: {42:5d}")     #    42

# ===== 입력 (input) =====

# 9. 기본 입력
name = input("이름을 입력하세요: ")
print(f"안녕하세요, {name}님!")

# 10. 숫자 입력 (형변환 필요)
age = int(input("나이를 입력하세요: "))
print(f"내년에 {age + 1}살입니다.")

# 11. 실수 입력
height = float(input("키를 입력하세요: "))
print(f"키: {height}cm")

# 12. 여러 값 입력 (공백 구분)
a, b = input("두 숫자 입력 (공백 구분): ").split()
print(f"a={a}, b={b}")

# 13. 여러 숫자 입력 + 형변환
x, y = map(int, input("두 정수 입력: ").split())
print(f"합: {x + y}")

# 14. 리스트로 여러 값 입력
nums = list(map(int, input("숫자들 입력: ").split()))
print(f"입력값: {nums}, 합계: {sum(nums)}")

# ===== 파일 입출력 =====

# 15. 파일 쓰기
with open("test.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")

# 16. 파일 읽기
# with open("test.txt", "r") as f:
#     content = f.read()
#     print(content)

# 17. 파일 한 줄씩 읽기
# with open("test.txt", "r") as f:
#     for line in f:
#         print(line.strip())
