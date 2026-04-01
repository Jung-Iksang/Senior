# =============================================================================
# Python 제어문, 반복문, 중첩 완벽 정리
# =============================================================================

# =============================================================================
# 1. 조건문 (Conditional Statements)
# =============================================================================

print("=" * 60)
print("1. 조건문 (Conditional Statements)")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1.1 if 문 기본
# -----------------------------------------------------------------------------
print("\n--- 1.1 if 문 기본 ---")

x = 10

# 기본 if
if x > 0:
    print(f"x={x}는 양수입니다")

# if-else
if x > 0:
    print("양수")
else:
    print("양수 아님")

# if-elif-else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"점수 {score} -> 학점 {grade}")

# -----------------------------------------------------------------------------
# 1.2 비교 연산자
# -----------------------------------------------------------------------------
print("\n--- 1.2 비교 연산자 ---")

a, b = 10, 20

print(f"a={a}, b={b}")
print(f"a == b: {a == b}")   # 같음
print(f"a != b: {a != b}")   # 다름
print(f"a > b: {a > b}")     # 크다
print(f"a < b: {a < b}")     # 작다
print(f"a >= b: {a >= b}")   # 크거나 같음
print(f"a <= b: {a <= b}")   # 작거나 같음

# 연속 비교 (Python 특징!)
x = 15
print(f"\nx={x}")
print(f"10 < x < 20: {10 < x < 20}")
print(f"10 < x < 12: {10 < x < 12}")
print(f"0 <= x <= 100: {0 <= x <= 100}")

# -----------------------------------------------------------------------------
# 1.3 논리 연산자
# -----------------------------------------------------------------------------
print("\n--- 1.3 논리 연산자 ---")

x, y = True, False

print(f"x={x}, y={y}")
print(f"x and y: {x and y}")  # 둘 다 True여야 True
print(f"x or y: {x or y}")    # 하나만 True여도 True
print(f"not x: {not x}")      # 반전

# 실제 활용
age = 25
has_license = True

if age >= 18 and has_license:
    print("운전 가능")

# 복합 조건
score = 85
attendance = 90

if score >= 80 and attendance >= 80:
    print("우수 학생")
elif score >= 80 or attendance >= 80:
    print("보통 학생")
else:
    print("노력 필요")

# -----------------------------------------------------------------------------
# 1.4 멤버십 연산자 (in, not in)
# -----------------------------------------------------------------------------
print("\n--- 1.4 멤버십 연산자 ---")

fruits = ["apple", "banana", "cherry"]
text = "Hello World"

print(f"fruits: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'grape' not in fruits: {'grape' not in fruits}")

print(f"\ntext: '{text}'")
print(f"'Hello' in text: {'Hello' in text}")
print(f"'hello' in text: {'hello' in text}")  # 대소문자 구분!

# 딕셔너리에서 (키 검사)
person = {"name": "Alice", "age": 25}
print(f"\nperson: {person}")
print(f"'name' in person: {'name' in person}")
print(f"'Alice' in person: {'Alice' in person}")  # 키만 검사!
print(f"'Alice' in person.values(): {'Alice' in person.values()}")

# -----------------------------------------------------------------------------
# 1.5 식별 연산자 (is, is not)
# -----------------------------------------------------------------------------
print("\n--- 1.5 식별 연산자 ---")

# is: 동일한 객체인지 (메모리 주소 비교)
# ==: 값이 같은지

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}, b = {b}, c = a")
print(f"a == b: {a == b}")  # True (값이 같음)
print(f"a is b: {a is b}")  # False (다른 객체)
print(f"a is c: {a is c}")  # True (같은 객체)

# None 비교는 is 사용
x = None
print(f"\nx is None: {x is None}")
print(f"x is not None: {x is not None}")

# 작은 정수는 캐싱됨 (-5 ~ 256)
x = 100
y = 100
print(f"\nx=100, y=100")
print(f"x is y: {x is y}")  # True (캐싱됨)

x = 1000
y = 1000
print(f"x=1000, y=1000")
print(f"x is y: {x is y}")  # False (캐싱 안됨)

# -----------------------------------------------------------------------------
# 1.6 삼항 연산자 (조건부 표현식)
# -----------------------------------------------------------------------------
print("\n--- 1.6 삼항 연산자 ---")

# 문법: 참값 if 조건 else 거짓값

age = 20
status = "성인" if age >= 18 else "미성년"
print(f"나이 {age}: {status}")

# 기존 if-else와 비교
if age >= 18:
    status = "성인"
else:
    status = "미성년"

# 중첩 삼항 연산자
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"점수 {score}: 학점 {grade}")

# 리스트에서 활용
numbers = [1, -2, 3, -4, 5]
abs_numbers = [x if x >= 0 else -x for x in numbers]
print(f"절대값: {numbers} -> {abs_numbers}")

# 함수 반환값
def get_status(age):
    return "성인" if age >= 18 else "미성년"

print(f"get_status(15): {get_status(15)}")
print(f"get_status(25): {get_status(25)}")

# -----------------------------------------------------------------------------
# 1.7 Truthy와 Falsy
# -----------------------------------------------------------------------------
print("\n--- 1.7 Truthy와 Falsy ---")

# Falsy 값들 (조건에서 False로 평가)
falsy_values = [False, None, 0, 0.0, "", [], {}, set(), (), 0j]

print("Falsy 값들:")
for val in falsy_values:
    print(f"  bool({repr(val):12}) = {bool(val)}")

# Truthy 예시
print("\nTruthy 예시:")
truthy_values = [True, 1, -1, "hello", [1], {"a": 1}, {1}, (1,)]
for val in truthy_values:
    print(f"  bool({repr(val):12}) = {bool(val)}")

# 실제 활용
name = ""
if name:
    print(f"이름: {name}")
else:
    print("이름이 비어있습니다")

items = []
if not items:
    print("리스트가 비어있습니다")

# -----------------------------------------------------------------------------
# 1.8 match-case (Python 3.10+)
# -----------------------------------------------------------------------------
print("\n--- 1.8 match-case (Python 3.10+) ---")

def get_day_type(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return "평일"
        case "Saturday" | "Sunday":
            return "주말"
        case _:
            return "알 수 없음"

print(f"Monday: {get_day_type('Monday')}")
print(f"Saturday: {get_day_type('Saturday')}")
print(f"Holiday: {get_day_type('Holiday')}")

# 패턴 매칭
def describe_point(point):
    match point:
        case (0, 0):
            return "원점"
        case (0, y):
            return f"Y축 위 ({y})"
        case (x, 0):
            return f"X축 위 ({x})"
        case (x, y):
            return f"좌표 ({x}, {y})"
        case _:
            return "유효하지 않음"

print(f"(0, 0): {describe_point((0, 0))}")
print(f"(0, 5): {describe_point((0, 5))}")
print(f"(3, 0): {describe_point((3, 0))}")
print(f"(3, 4): {describe_point((3, 4))}")

# 가드 조건 (if)
def categorize_number(n):
    match n:
        case x if x < 0:
            return "음수"
        case 0:
            return "영"
        case x if x > 0:
            return "양수"

print(f"-5: {categorize_number(-5)}")
print(f"0: {categorize_number(0)}")
print(f"10: {categorize_number(10)}")


# =============================================================================
# 2. 반복문 (Loop Statements)
# =============================================================================

print("\n" + "=" * 60)
print("2. 반복문 (Loop Statements)")
print("=" * 60)

# -----------------------------------------------------------------------------
# 2.1 for 문 기본
# -----------------------------------------------------------------------------
print("\n--- 2.1 for 문 기본 ---")

# 리스트 순회
fruits = ["apple", "banana", "cherry"]
print("리스트 순회:")
for fruit in fruits:
    print(f"  {fruit}")

# 문자열 순회
print("\n문자열 순회:")
for char in "Hello":
    print(f"  {char}")

# 튜플 순회
print("\n튜플 순회:")
for item in (1, 2, 3):
    print(f"  {item}")

# 딕셔너리 순회
print("\n딕셔너리 순회:")
person = {"name": "Alice", "age": 25, "city": "Seoul"}

print("키 순회:")
for key in person:
    print(f"  {key}")

print("값 순회:")
for value in person.values():
    print(f"  {value}")

print("키-값 순회:")
for key, value in person.items():
    print(f"  {key}: {value}")

# 세트 순회
print("\n세트 순회:")
for num in {3, 1, 4, 1, 5}:
    print(f"  {num}")

# -----------------------------------------------------------------------------
# 2.2 range() 함수
# -----------------------------------------------------------------------------
print("\n--- 2.2 range() 함수 ---")

# range(stop): 0부터 stop-1까지
print("range(5):", list(range(5)))

# range(start, stop): start부터 stop-1까지
print("range(2, 7):", list(range(2, 7)))

# range(start, stop, step): step 간격
print("range(0, 10, 2):", list(range(0, 10, 2)))
print("range(10, 0, -1):", list(range(10, 0, -1)))
print("range(10, 0, -2):", list(range(10, 0, -2)))

# for문에서 사용
print("\nrange(5)로 반복:")
for i in range(5):
    print(f"  i = {i}")

# 인덱스로 리스트 접근
fruits = ["apple", "banana", "cherry"]
print("\n인덱스로 접근:")
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")

# -----------------------------------------------------------------------------
# 2.3 enumerate() 함수
# -----------------------------------------------------------------------------
print("\n--- 2.3 enumerate() 함수 ---")

fruits = ["apple", "banana", "cherry"]

# 기본 사용
print("enumerate 기본:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# 시작 인덱스 지정
print("\nenumerate(fruits, 1):")
for index, fruit in enumerate(fruits, 1):
    print(f"  {index}: {fruit}")

# enumerate 객체 확인
print(f"\nlist(enumerate(fruits)): {list(enumerate(fruits))}")

# 실제 활용: 특정 조건 인덱스 찾기
numbers = [10, 20, 30, 20, 40]
target = 20
print(f"\n{target}의 위치:")
for i, num in enumerate(numbers):
    if num == target:
        print(f"  인덱스 {i}")

# -----------------------------------------------------------------------------
# 2.4 zip() 함수
# -----------------------------------------------------------------------------
print("\n--- 2.4 zip() 함수 ---")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Seoul", "Busan", "Daegu"]

# 두 리스트 묶기
print("두 리스트 zip:")
for name, age in zip(names, ages):
    print(f"  {name}: {age}세")

# 세 개 이상 묶기
print("\n세 리스트 zip:")
for name, age, city in zip(names, ages, cities):
    print(f"  {name}, {age}세, {city}")

# zip 객체 확인
print(f"\nlist(zip(names, ages)): {list(zip(names, ages))}")

# 길이가 다른 경우 (짧은 쪽에 맞춤)
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
print(f"\n길이 다른 zip: {list(zip(a, b))}")

# zip_longest 사용 (긴 쪽에 맞춤)
from itertools import zip_longest
print(f"zip_longest: {list(zip_longest(a, b, fillvalue='?'))}")

# 딕셔너리 생성
keys = ["name", "age"]
values = ["Alice", 25]
d = dict(zip(keys, values))
print(f"\ndict(zip(keys, values)): {d}")

# unzip (역방향)
pairs = [("a", 1), ("b", 2), ("c", 3)]
letters, numbers = zip(*pairs)
print(f"\nunzip: letters={letters}, numbers={numbers}")

# -----------------------------------------------------------------------------
# 2.5 while 문 기본
# -----------------------------------------------------------------------------
print("\n--- 2.5 while 문 기본 ---")

# 기본 사용
print("1부터 5까지:")
i = 1
while i <= 5:
    print(f"  {i}")
    i += 1

# 조건이 False가 될 때까지
print("\n10에서 시작해서 절반씩:")
n = 10
while n >= 1:
    print(f"  {n}")
    n //= 2

# 무한 루프 (break로 탈출)
print("\n무한 루프 예시:")
count = 0
while True:
    count += 1
    print(f"  반복 {count}")
    if count >= 3:
        print("  break!")
        break

# 입력 받기 예시 (주석 처리)
# while True:
#     user_input = input("입력하세요 (q로 종료): ")
#     if user_input == 'q':
#         break
#     print(f"입력: {user_input}")

# -----------------------------------------------------------------------------
# 2.6 break, continue, else
# -----------------------------------------------------------------------------
print("\n--- 2.6 break, continue, else ---")

# break: 루프 즉시 종료
print("[break 예시]")
for i in range(10):
    if i == 5:
        print(f"  i={i}에서 break")
        break
    print(f"  i={i}")

# continue: 현재 반복 건너뛰고 다음으로
print("\n[continue 예시]")
for i in range(6):
    if i == 3:
        print(f"  i={i} 건너뜀")
        continue
    print(f"  i={i}")

# else: 루프가 break 없이 완료되면 실행
print("\n[for-else 예시]")

# break 없이 완료
print("break 없이 완료:")
for i in range(3):
    print(f"  i={i}")
else:
    print("  else 블록 실행됨!")

# break로 종료
print("\nbreak로 종료:")
for i in range(5):
    print(f"  i={i}")
    if i == 2:
        break
else:
    print("  else 블록 실행됨!")  # 실행 안됨

# 실제 활용: 검색
print("\n[else 실제 활용 - 검색]")
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print(f"  {target} 찾음!")
        break
else:
    print(f"  {target} 없음")

# while-else
print("\n[while-else 예시]")
i = 0
while i < 3:
    print(f"  i={i}")
    i += 1
else:
    print("  while 완료, else 실행")

# -----------------------------------------------------------------------------
# 2.7 pass 문
# -----------------------------------------------------------------------------
print("\n--- 2.7 pass 문 ---")

# 빈 블록을 위한 플레이스홀더
for i in range(3):
    pass  # 나중에 구현

# 빈 함수
def todo_function():
    pass

# 빈 클래스
class TodoClass:
    pass

# 조건문에서
x = 10
if x > 5:
    pass  # 나중에 처리
else:
    print("5 이하")

print("pass는 아무것도 하지 않는 문장입니다")

# -----------------------------------------------------------------------------
# 2.8 반복문 고급 패턴
# -----------------------------------------------------------------------------
print("\n--- 2.8 반복문 고급 패턴 ---")

# reversed() - 역순 반복
print("[reversed]")
for i in reversed(range(5)):
    print(f"  {i}", end=" ")
print()

# sorted() - 정렬된 순서로 반복
print("\n[sorted]")
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"원본: {numbers}")
print(f"정렬: ", end="")
for num in sorted(numbers):
    print(num, end=" ")
print()

# 역순 정렬
print(f"역순 정렬: ", end="")
for num in sorted(numbers, reverse=True):
    print(num, end=" ")
print()

# filter() - 조건에 맞는 요소만
print("\n[filter]")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = filter(lambda x: x % 2 == 0, numbers)
print(f"짝수만: {list(evens)}")

# map() - 모든 요소에 함수 적용
print("\n[map]")
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x**2, numbers)
print(f"제곱: {list(squares)}")

# map과 filter 조합
print("\n[map + filter]")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
print(f"짝수의 제곱: {list(result)}")


# =============================================================================
# 3. 중첩 반복문 (Nested Loops)
# =============================================================================

print("\n" + "=" * 60)
print("3. 중첩 반복문 (Nested Loops)")
print("=" * 60)

# -----------------------------------------------------------------------------
# 3.1 기본 중첩 for문
# -----------------------------------------------------------------------------
print("\n--- 3.1 기본 중첩 for문 ---")

# 2중 for문
print("2중 for문:")
for i in range(3):
    for j in range(3):
        print(f"  ({i}, {j})")

# 구구단
print("\n구구단 (2~4단):")
for i in range(2, 5):
    print(f"{i}단: ", end="")
    for j in range(1, 10):
        print(f"{i}x{j}={i*j:2}", end=" ")
    print()

# -----------------------------------------------------------------------------
# 3.2 중첩 반복문으로 패턴 만들기
# -----------------------------------------------------------------------------
print("\n--- 3.2 패턴 만들기 ---")

# 직각삼각형 (왼쪽 정렬)
print("[직각삼각형 - 왼쪽]")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# 직각삼각형 (오른쪽 정렬)
print("\n[직각삼각형 - 오른쪽]")
for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()

# 역삼각형
print("\n[역삼각형]")
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# 피라미드
print("\n[피라미드]")
for i in range(1, 6):
    print(" " * (5 - i) + "*" * (2 * i - 1))

# 다이아몬드
print("\n[다이아몬드]")
n = 5
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 숫자 패턴
print("\n[숫자 패턴]")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# -----------------------------------------------------------------------------
# 3.3 2차원 리스트 순회
# -----------------------------------------------------------------------------
print("\n--- 3.3 2차원 리스트 순회 ---")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 기본 순회
print("2차원 리스트 순회:")
for row in matrix:
    for item in row:
        print(f"  {item}", end="")
    print()

# 인덱스로 접근
print("\n인덱스로 접근:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"  matrix[{i}][{j}] = {matrix[i][j]}")

# enumerate 사용
print("\nenumerate 사용:")
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        print(f"  ({i},{j}): {val}")

# 행 합계
print("\n행 합계:")
for i, row in enumerate(matrix):
    print(f"  행 {i}: {sum(row)}")

# 열 합계
print("\n열 합계:")
for j in range(len(matrix[0])):
    col_sum = sum(matrix[i][j] for i in range(len(matrix)))
    print(f"  열 {j}: {col_sum}")

# 대각선 합계
diag_sum = sum(matrix[i][i] for i in range(len(matrix)))
anti_diag_sum = sum(matrix[i][len(matrix)-1-i] for i in range(len(matrix)))
print(f"\n주대각선 합: {diag_sum}")
print(f"반대각선 합: {anti_diag_sum}")

# -----------------------------------------------------------------------------
# 3.4 중첩 반복문과 break/continue
# -----------------------------------------------------------------------------
print("\n--- 3.4 중첩 반복문과 break/continue ---")

# break는 가장 안쪽 루프만 탈출
print("[break는 안쪽 루프만 탈출]")
for i in range(3):
    print(f"외부 {i}:")
    for j in range(5):
        if j == 2:
            print(f"    내부 {j}에서 break")
            break
        print(f"    내부 {j}")

# 전체 루프 탈출하기 (플래그 사용)
print("\n[플래그로 전체 탈출]")
found = False
for i in range(3):
    if found:
        break
    for j in range(3):
        print(f"  ({i}, {j})")
        if i == 1 and j == 1:
            print("  찾음! 전체 탈출")
            found = True
            break

# for-else 활용
print("\n[for-else로 전체 탈출]")
for i in range(3):
    for j in range(3):
        print(f"  ({i}, {j})")
        if i == 1 and j == 1:
            print("  찾음!")
            break
    else:
        continue  # 내부 루프가 break 없이 끝나면 계속
    break  # 내부 루프가 break로 끝나면 외부도 break

# 함수로 감싸서 return 사용
def find_target():
    for i in range(3):
        for j in range(3):
            print(f"  ({i}, {j})")
            if i == 1 and j == 1:
                return (i, j)
    return None

print("\n[함수 return으로 탈출]")
result = find_target()
print(f"결과: {result}")

# -----------------------------------------------------------------------------
# 3.5 중첩 while문
# -----------------------------------------------------------------------------
print("\n--- 3.5 중첩 while문 ---")

print("중첩 while:")
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(f"  ({i}, {j})")
        j += 1
    i += 1

# for와 while 혼합
print("\n[for + while 혼합]")
for i in range(3):
    j = 0
    while j < 3:
        print(f"  ({i}, {j})", end=" ")
        j += 1
    print()

# -----------------------------------------------------------------------------
# 3.6 3중 이상 중첩
# -----------------------------------------------------------------------------
print("\n--- 3.6 3중 중첩 ---")

# 3차원 리스트 순회
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

print("3차원 리스트:")
for i, plane in enumerate(cube):
    print(f"면 {i}:")
    for j, row in enumerate(plane):
        for k, val in enumerate(row):
            print(f"  [{i}][{j}][{k}] = {val}")

# 모든 조합
print("\n[모든 조합]")
colors = ["R", "G"]
sizes = ["S", "M"]
types = ["A", "B"]

for color in colors:
    for size in sizes:
        for type_ in types:
            print(f"  {color}-{size}-{type_}")

# itertools.product 사용 (더 깔끔)
from itertools import product

print("\n[itertools.product 사용]")
for combo in product(colors, sizes, types):
    print(f"  {'-'.join(combo)}")


# =============================================================================
# 4. 중첩 조건문 (Nested Conditionals)
# =============================================================================

print("\n" + "=" * 60)
print("4. 중첩 조건문 (Nested Conditionals)")
print("=" * 60)

# -----------------------------------------------------------------------------
# 4.1 기본 중첩 if
# -----------------------------------------------------------------------------
print("\n--- 4.1 기본 중첩 if ---")

age = 25
has_id = True
has_ticket = True

if age >= 18:
    print("성인입니다")
    if has_id:
        print("  신분증 확인됨")
        if has_ticket:
            print("    입장 가능!")
        else:
            print("    티켓이 없습니다")
    else:
        print("  신분증이 필요합니다")
else:
    print("미성년자입니다")
    if has_ticket:
        print("  보호자 동반 시 입장 가능")

# -----------------------------------------------------------------------------
# 4.2 복잡한 조건 처리
# -----------------------------------------------------------------------------
print("\n--- 4.2 복잡한 조건 처리 ---")

# 안 좋은 예: 깊은 중첩
def check_access_bad(user):
    if user is not None:
        if user.get("active"):
            if user.get("role") == "admin":
                if user.get("verified"):
                    return "접근 허용"
                else:
                    return "인증 필요"
            else:
                return "권한 없음"
        else:
            return "비활성 계정"
    else:
        return "사용자 없음"

# 좋은 예: 조기 반환 (Early Return)
def check_access_good(user):
    if user is None:
        return "사용자 없음"
    if not user.get("active"):
        return "비활성 계정"
    if user.get("role") != "admin":
        return "권한 없음"
    if not user.get("verified"):
        return "인증 필요"
    return "접근 허용"

# 테스트
users = [
    None,
    {"active": False},
    {"active": True, "role": "user"},
    {"active": True, "role": "admin", "verified": False},
    {"active": True, "role": "admin", "verified": True}
]

print("조기 반환 패턴:")
for user in users:
    print(f"  {user} -> {check_access_good(user)}")

# -----------------------------------------------------------------------------
# 4.3 조건 결합
# -----------------------------------------------------------------------------
print("\n--- 4.3 조건 결합 ---")

# 중첩 if를 and로 결합
age = 25
income = 50000
credit_score = 700

# 중첩 방식
if age >= 18:
    if income >= 30000:
        if credit_score >= 650:
            print("중첩: 대출 승인")

# 결합 방식
if age >= 18 and income >= 30000 and credit_score >= 650:
    print("결합: 대출 승인")

# 복잡한 조건 분리
is_adult = age >= 18
has_income = income >= 30000
good_credit = credit_score >= 650

if is_adult and has_income and good_credit:
    print("분리: 대출 승인")


# =============================================================================
# 5. 반복문과 조건문 결합
# =============================================================================

print("\n" + "=" * 60)
print("5. 반복문과 조건문 결합")
print("=" * 60)

# -----------------------------------------------------------------------------
# 5.1 반복 중 조건 처리
# -----------------------------------------------------------------------------
print("\n--- 5.1 반복 중 조건 처리 ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 홀짝 분류
print("홀짝 분류:")
for num in numbers:
    if num % 2 == 0:
        print(f"  {num}: 짝수")
    else:
        print(f"  {num}: 홀수")

# 특정 조건만 처리
print("\n3의 배수만:")
for num in numbers:
    if num % 3 == 0:
        print(f"  {num}")

# -----------------------------------------------------------------------------
# 5.2 검색 패턴
# -----------------------------------------------------------------------------
print("\n--- 5.2 검색 패턴 ---")

# 선형 검색
def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

numbers = [64, 34, 25, 12, 22, 11, 90]
target = 22
result = linear_search(numbers, target)
print(f"{target} 위치: {result}")

# 모든 위치 찾기
def find_all(arr, target):
    positions = []
    for i, val in enumerate(arr):
        if val == target:
            positions.append(i)
    return positions

numbers = [1, 2, 3, 2, 4, 2, 5]
target = 2
print(f"{target}의 모든 위치: {find_all(numbers, target)}")

# 조건에 맞는 요소 찾기
def find_first(arr, condition):
    for item in arr:
        if condition(item):
            return item
    return None

numbers = [1, 3, 5, 8, 9, 12]
first_even = find_first(numbers, lambda x: x % 2 == 0)
print(f"첫 번째 짝수: {first_even}")

# -----------------------------------------------------------------------------
# 5.3 필터링과 변환
# -----------------------------------------------------------------------------
print("\n--- 5.3 필터링과 변환 ---")

numbers = list(range(1, 21))
print(f"원본: {numbers}")

# 조건으로 필터링
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print(f"짝수: {evens}")

# 리스트 컴프리헨션
evens = [num for num in numbers if num % 2 == 0]
print(f"컴프리헨션: {evens}")

# 조건부 변환
modified = []
for num in numbers:
    if num % 2 == 0:
        modified.append(num * 2)
    else:
        modified.append(num)
print(f"짝수만 2배: {modified}")

# 컴프리헨션으로
modified = [num * 2 if num % 2 == 0 else num for num in numbers]
print(f"컴프리헨션: {modified}")

# -----------------------------------------------------------------------------
# 5.4 집계 패턴
# -----------------------------------------------------------------------------
print("\n--- 5.4 집계 패턴 ---")

numbers = [85, 90, 78, 92, 88, 76, 95, 89]
print(f"점수: {numbers}")

# 합계, 평균
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(f"합계: {total}, 평균: {average:.2f}")

# 최대, 최소
max_val = numbers[0]
min_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
print(f"최대: {max_val}, 최소: {min_val}")

# 조건부 카운트
above_80 = 0
for num in numbers:
    if num >= 80:
        above_80 += 1
print(f"80점 이상: {above_80}명")

# 그룹핑
grades = {"A": [], "B": [], "C": [], "F": []}
for score in numbers:
    if score >= 90:
        grades["A"].append(score)
    elif score >= 80:
        grades["B"].append(score)
    elif score >= 70:
        grades["C"].append(score)
    else:
        grades["F"].append(score)

print("학점별 분류:")
for grade, scores in grades.items():
    print(f"  {grade}: {scores}")


# =============================================================================
# 6. 실전 예제
# =============================================================================

print("\n" + "=" * 60)
print("6. 실전 예제")
print("=" * 60)

# -----------------------------------------------------------------------------
# 6.1 소수 판별
# -----------------------------------------------------------------------------
print("\n--- 6.1 소수 판별 ---")

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# 1~30 중 소수
primes = [n for n in range(1, 31) if is_prime(n)]
print(f"1~30 소수: {primes}")

# -----------------------------------------------------------------------------
# 6.2 피보나치 수열
# -----------------------------------------------------------------------------
print("\n--- 6.2 피보나치 수열 ---")

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

print(f"피보나치 10개: {fibonacci(10)}")

# -----------------------------------------------------------------------------
# 6.3 버블 정렬
# -----------------------------------------------------------------------------
print("\n--- 6.3 버블 정렬 ---")

def bubble_sort(arr):
    arr = arr.copy()  # 원본 보존
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
print(f"원본: {numbers}")
print(f"정렬: {bubble_sort(numbers)}")

# -----------------------------------------------------------------------------
# 6.4 행렬 연산
# -----------------------------------------------------------------------------
print("\n--- 6.4 행렬 연산 ---")

# 행렬 덧셈
def matrix_add(a, b):
    result = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result

# 행렬 곱셈
def matrix_multiply(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])

    if cols_a != rows_b:
        raise ValueError("행렬 크기가 맞지 않습니다")

    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print(f"A = {A}")
print(f"B = {B}")
print(f"A + B = {matrix_add(A, B)}")
print(f"A * B = {matrix_multiply(A, B)}")

# -----------------------------------------------------------------------------
# 6.5 텍스트 분석
# -----------------------------------------------------------------------------
print("\n--- 6.5 텍스트 분석 ---")

text = """Python is a programming language.
Python is easy to learn.
Python is powerful and versatile."""

# 단어 빈도 분석
words = text.lower().replace(".", "").replace(",", "").split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("단어 빈도:")
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"  {word}: {count}")

# 문장별 단어 수
sentences = text.strip().split('\n')
print("\n문장별 단어 수:")
for i, sentence in enumerate(sentences, 1):
    word_count = len(sentence.split())
    print(f"  문장 {i}: {word_count}단어")

# -----------------------------------------------------------------------------
# 6.6 간단한 게임 루프 구조
# -----------------------------------------------------------------------------
print("\n--- 6.6 게임 루프 구조 (시뮬레이션) ---")

import random

def simple_game_simulation():
    score = 0
    lives = 3
    level = 1

    # 시뮬레이션 (실제로는 사용자 입력 받음)
    actions = ["hit", "miss", "hit", "hit", "miss", "miss", "miss"]

    print("게임 시작!")

    for turn, action in enumerate(actions, 1):
        print(f"\n턴 {turn} (레벨 {level}, 생명 {lives}):")

        if action == "hit":
            points = level * 10
            score += points
            print(f"  성공! +{points}점 (총 {score}점)")

            if score >= level * 50:
                level += 1
                print(f"  레벨 업! -> 레벨 {level}")
        else:
            lives -= 1
            print(f"  실패! 생명 -1 (남은 생명: {lives})")

            if lives <= 0:
                print("\n게임 오버!")
                break
    else:
        print("\n모든 턴 완료!")

    print(f"\n최종 점수: {score}, 도달 레벨: {level}")

simple_game_simulation()


# =============================================================================
# 7. 정리
# =============================================================================

print("\n" + "=" * 60)
print("7. 제어문/반복문 정리")
print("=" * 60)

print("""
[조건문]
- if, elif, else: 조건 분기
- 비교 연산자: ==, !=, <, >, <=, >=
- 논리 연산자: and, or, not
- 멤버십: in, not in
- 식별: is, is not
- 삼항 연산자: 값1 if 조건 else 값2
- match-case: 패턴 매칭 (Python 3.10+)

[반복문]
- for: 이터러블 순회
- while: 조건이 참인 동안 반복
- range(): 숫자 시퀀스 생성
- enumerate(): 인덱스와 함께 순회
- zip(): 여러 이터러블 동시 순회

[제어 키워드]
- break: 루프 즉시 종료
- continue: 현재 반복 건너뛰기
- pass: 아무것도 하지 않음
- else: 루프가 break 없이 완료되면 실행

[중첩]
- 다중 루프: 외부/내부 루프 구조
- break는 가장 안쪽 루프만 탈출
- 전체 탈출: 플래그, for-else, 함수 return

[권장 패턴]
- 조기 반환으로 중첩 줄이기
- 컴프리헨션으로 간결하게 표현
- 적절한 함수 분리
""")

print("프로그램 종료")
