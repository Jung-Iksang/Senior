# =============================================================================
# Python 튜플(Tuple) & 딕셔너리(Dictionary) 정리
# =============================================================================

# =============================================================================
# 1. 튜플 (Tuple) - 불변(immutable)한 순서가 있는 컬렉션
# =============================================================================

print("=" * 60)
print("1. 튜플 (Tuple)")
print("=" * 60)

# -----------------------------------------------------------------------------
# 1.1 튜플 생성
# -----------------------------------------------------------------------------
print("\n--- 1.1 튜플 생성 ---")

t1 = (1, 2, 3)              # 기본 생성
t2 = 1, 2, 3                # 괄호 생략 가능
t3 = (1,)                   # 요소 1개일 때 콤마 필수!
t4 = ()                     # 빈 튜플
t5 = tuple([1, 2, 3])       # 리스트 -> 튜플 변환
t6 = tuple("hello")         # 문자열 -> 튜플 변환

print(f"t1 = (1, 2, 3): {t1}")
print(f"t2 = 1, 2, 3: {t2}")
print(f"t3 = (1,): {t3}, type: {type(t3)}")
print(f"t4 = (): {t4}")
print(f"t5 = tuple([1,2,3]): {t5}")
print(f"t6 = tuple('hello'): {t6}")

# 주의: 콤마 없으면 튜플이 아님!
not_tuple = (1)
print(f"(1)의 타입: {type(not_tuple)}")  # int

# -----------------------------------------------------------------------------
# 1.2 튜플 인덱싱 & 슬라이싱
# -----------------------------------------------------------------------------
print("\n--- 1.2 튜플 인덱싱 & 슬라이싱 ---")

t = (10, 20, 30, 40, 50)

print(f"튜플: {t}")
print(f"t[0]: {t[0]}")          # 첫 번째 요소
print(f"t[-1]: {t[-1]}")        # 마지막 요소
print(f"t[1:3]: {t[1:3]}")      # 인덱스 1~2
print(f"t[:3]: {t[:3]}")        # 처음~인덱스 2
print(f"t[2:]: {t[2:]}")        # 인덱스 2~끝
print(f"t[::2]: {t[::2]}")      # 2칸씩 건너뛰기
print(f"t[::-1]: {t[::-1]}")    # 역순

# -----------------------------------------------------------------------------
# 1.3 튜플 연산
# -----------------------------------------------------------------------------
print("\n--- 1.3 튜플 연산 ---")

t1 = (1, 2)
t2 = (3, 4)

print(f"t1 = {t1}, t2 = {t2}")
print(f"t1 + t2 (연결): {t1 + t2}")
print(f"t1 * 3 (반복): {t1 * 3}")
print(f"len(t1): {len(t1)}")
print(f"2 in t1: {2 in t1}")
print(f"5 in t1: {5 in t1}")

# -----------------------------------------------------------------------------
# 1.4 튜플 메서드
# -----------------------------------------------------------------------------
print("\n--- 1.4 튜플 메서드 ---")

t = (1, 2, 2, 3, 2, 4, 5)

print(f"튜플: {t}")
print(f"t.count(2): {t.count(2)}")    # 2의 개수
print(f"t.index(3): {t.index(3)}")    # 3의 첫 번째 위치
print(f"max(t): {max(t)}")            # 최대값
print(f"min(t): {min(t)}")            # 최소값
print(f"sum(t): {sum(t)}")            # 합계

# -----------------------------------------------------------------------------
# 1.5 패킹 & 언패킹
# -----------------------------------------------------------------------------
print("\n--- 1.5 패킹 & 언패킹 ---")

# 패킹: 여러 값을 하나의 튜플로 묶기
packed = 1, 2, 3
print(f"패킹 - packed = 1, 2, 3: {packed}")

# 언패킹: 튜플을 여러 변수로 분리
a, b, c = packed
print(f"언패킹 - a, b, c = packed: a={a}, b={b}, c={c}")

# 확장 언패킹 (* 사용)
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"first, *middle, last = {numbers}")
print(f"  first={first}, middle={middle}, last={last}")

*start, end = numbers
print(f"*start, end = {numbers}")
print(f"  start={start}, end={end}")

# 값 교환 (swap)
x, y = 10, 20
print(f"교환 전: x={x}, y={y}")
x, y = y, x
print(f"교환 후: x={x}, y={y}")

# -----------------------------------------------------------------------------
# 1.6 튜플의 불변성
# -----------------------------------------------------------------------------
print("\n--- 1.6 튜플의 불변성 ---")

t = (1, 2, 3)
print(f"튜플: {t}")
print("t[0] = 10 시도하면 -> TypeError 발생!")
# t[0] = 10  # TypeError: 'tuple' object does not support item assignment

# 단, 튜플 안의 가변 객체는 수정 가능
t = (1, 2, [3, 4])
print(f"튜플 안에 리스트: {t}")
t[2][0] = 100
print(f"t[2][0] = 100 후: {t}")

# -----------------------------------------------------------------------------
# 1.7 튜플 활용 예시
# -----------------------------------------------------------------------------
print("\n--- 1.7 튜플 활용 예시 ---")

# 함수에서 여러 값 반환
def get_min_max(numbers):
    return min(numbers), max(numbers)

result = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"get_min_max 반환값: {result}")
min_val, max_val = get_min_max([3, 1, 4, 1, 5, 9, 2, 6])
print(f"언패킹: min={min_val}, max={max_val}")

# 딕셔너리 키로 사용 (리스트는 불가!)
locations = {
    (37.5, 127.0): "서울",
    (35.1, 129.0): "부산"
}
print(f"좌표 딕셔너리: {locations}")
print(f"(37.5, 127.0) 위치: {locations[(37.5, 127.0)]}")


# =============================================================================
# 2. 딕셔너리 (Dictionary) - 키-값 쌍의 컬렉션
# =============================================================================

print("\n" + "=" * 60)
print("2. 딕셔너리 (Dictionary)")
print("=" * 60)

# -----------------------------------------------------------------------------
# 2.1 딕셔너리 생성
# -----------------------------------------------------------------------------
print("\n--- 2.1 딕셔너리 생성 ---")

d1 = {"name": "Alice", "age": 25}       # 기본 생성
d2 = dict(name="Alice", age=25)         # dict() 사용
d3 = {}                                  # 빈 딕셔너리
d4 = dict()                              # 빈 딕셔너리
d5 = dict([("a", 1), ("b", 2)])         # 리스트로 생성
d6 = dict(zip(["a", "b"], [1, 2]))      # zip으로 생성

print(f'd1 = {{"name": "Alice", "age": 25}}: {d1}')
print(f"d2 = dict(name='Alice', age=25): {d2}")
print(f"d3 = {{}}: {d3}")
print(f'd5 = dict([("a", 1), ("b", 2)]): {d5}')
print(f'd6 = dict(zip(["a", "b"], [1, 2])): {d6}')

# -----------------------------------------------------------------------------
# 2.2 딕셔너리 접근
# -----------------------------------------------------------------------------
print("\n--- 2.2 딕셔너리 접근 ---")

person = {"name": "Alice", "age": 25, "city": "Seoul"}

print(f"딕셔너리: {person}")
print(f'person["name"]: {person["name"]}')
print(f'person.get("age"): {person.get("age")}')
print(f'person.get("job"): {person.get("job")}')  # 없으면 None
print(f'person.get("job", "없음"): {person.get("job", "없음")}')  # 기본값 지정

# 키 존재 확인
print(f'"name" in person: {"name" in person}')
print(f'"job" in person: {"job" in person}')

# -----------------------------------------------------------------------------
# 2.3 딕셔너리 수정/추가/삭제
# -----------------------------------------------------------------------------
print("\n--- 2.3 딕셔너리 수정/추가/삭제 ---")

d = {"a": 1, "b": 2}
print(f"원본: {d}")

# 수정
d["a"] = 100
print(f'd["a"] = 100 후: {d}')

# 추가
d["c"] = 3
print(f'd["c"] = 3 후: {d}')

# 여러 개 추가/수정
d.update({"d": 4, "e": 5})
print(f'd.update({{"d": 4, "e": 5}}) 후: {d}')

# setdefault: 키가 없으면 추가, 있으면 기존 값 반환
result = d.setdefault("f", 6)
print(f'd.setdefault("f", 6): {result}, 딕셔너리: {d}')
result = d.setdefault("a", 999)
print(f'd.setdefault("a", 999): {result}, 딕셔너리: {d}')

# 삭제
del d["f"]
print(f'del d["f"] 후: {d}')

popped = d.pop("e")
print(f'd.pop("e"): {popped}, 딕셔너리: {d}')

# pop with default (키 없어도 에러 안남)
popped = d.pop("z", "없음")
print(f'd.pop("z", "없음"): {popped}')

# popitem: 마지막 항목 제거 (Python 3.7+)
d = {"x": 1, "y": 2, "z": 3}
item = d.popitem()
print(f'd.popitem(): {item}, 딕셔너리: {d}')

# clear: 전체 삭제
d.clear()
print(f'd.clear() 후: {d}')

# -----------------------------------------------------------------------------
# 2.4 딕셔너리 메서드
# -----------------------------------------------------------------------------
print("\n--- 2.4 딕셔너리 메서드 ---")

d = {"a": 1, "b": 2, "c": 3}

# keys(), values(), items()
print(f"딕셔너리: {d}")
print(f"d.keys(): {d.keys()}")
print(f"d.values(): {d.values()}")
print(f"d.items(): {d.items()}")

# 리스트로 변환
print(f"list(d.keys()): {list(d.keys())}")
print(f"list(d.values()): {list(d.values())}")
print(f"list(d.items()): {list(d.items())}")

# copy (얕은 복사)
d2 = d.copy()
print(f"d.copy(): {d2}")

# fromkeys: 동일한 값으로 딕셔너리 생성
keys = ["x", "y", "z"]
d3 = dict.fromkeys(keys, 0)
print(f"dict.fromkeys(['x','y','z'], 0): {d3}")

# -----------------------------------------------------------------------------
# 2.5 딕셔너리 순회
# -----------------------------------------------------------------------------
print("\n--- 2.5 딕셔너리 순회 ---")

student = {"name": "Bob", "age": 20, "grade": "A"}

# 키 순회
print("키 순회:")
for key in student:
    print(f"  {key}")

# 값 순회
print("값 순회:")
for value in student.values():
    print(f"  {value}")

# 키-값 순회
print("키-값 순회:")
for key, value in student.items():
    print(f"  {key}: {value}")

# enumerate와 함께
print("enumerate 사용:")
for i, (key, value) in enumerate(student.items()):
    print(f"  {i}: {key} = {value}")

# -----------------------------------------------------------------------------
# 2.6 딕셔너리 컴프리헨션
# -----------------------------------------------------------------------------
print("\n--- 2.6 딕셔너리 컴프리헨션 ---")

# 기본 형태
squares = {x: x**2 for x in range(1, 6)}
print(f"{{x: x**2 for x in range(1, 6)}}: {squares}")

# 조건 포함
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"짝수만 제곱: {even_squares}")

# 키-값 변환
original = {"a": 1, "b": 2, "c": 3}
reversed_d = {v: k for k, v in original.items()}
print(f"키-값 교환: {original} -> {reversed_d}")

# 문자열에서 문자 카운트
text = "hello"
char_count = {char: text.count(char) for char in set(text)}
print(f"'hello' 문자 카운트: {char_count}")

# 조건부 값
numbers = [1, 2, 3, 4, 5]
labels = {n: "짝수" if n % 2 == 0 else "홀수" for n in numbers}
print(f"홀짝 라벨: {labels}")

# -----------------------------------------------------------------------------
# 2.7 중첩 딕셔너리
# -----------------------------------------------------------------------------
print("\n--- 2.7 중첩 딕셔너리 ---")

students = {
    "Alice": {"age": 20, "grade": "A", "subjects": ["Math", "English"]},
    "Bob": {"age": 22, "grade": "B", "subjects": ["Science", "History"]}
}

print("학생 정보:")
print(f"  students: {students}")
print(f'  students["Alice"]: {students["Alice"]}')
print(f'  students["Alice"]["age"]: {students["Alice"]["age"]}')
print(f'  students["Alice"]["subjects"][0]: {students["Alice"]["subjects"][0]}')

# 중첩 딕셔너리 추가
students["Charlie"] = {"age": 21, "grade": "A", "subjects": ["Art"]}
print(f'Charlie 추가 후: {students["Charlie"]}')

# 중첩 값 수정
students["Alice"]["grade"] = "A+"
print(f'Alice grade 수정 후: {students["Alice"]["grade"]}')

# 중첩 딕셔너리 순회
print("\n전체 학생 정보 출력:")
for name, info in students.items():
    print(f"  {name}: 나이={info['age']}, 학점={info['grade']}")

# -----------------------------------------------------------------------------
# 2.8 딕셔너리 병합
# -----------------------------------------------------------------------------
print("\n--- 2.8 딕셔너리 병합 ---")

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {"a": 100, "e": 5}  # 'a' 키 중복

# update 사용
merged1 = d1.copy()
merged1.update(d2)
print(f"update 사용: {merged1}")

# ** 연산자 사용 (Python 3.5+)
merged2 = {**d1, **d2}
print(f"** 연산자 사용: {merged2}")

# | 연산자 사용 (Python 3.9+)
merged3 = d1 | d2
print(f"| 연산자 사용: {merged3}")

# 중복 키가 있는 경우 (나중 값이 우선)
merged4 = {**d1, **d3}
print(f"중복 키 병합 (d1={d1}, d3={d3}): {merged4}")

# |= 연산자 (제자리 병합, Python 3.9+)
d1_copy = d1.copy()
d1_copy |= d2
print(f"|= 연산자 사용: {d1_copy}")

# -----------------------------------------------------------------------------
# 2.9 유용한 딕셔너리 패턴
# -----------------------------------------------------------------------------
print("\n--- 2.9 유용한 딕셔너리 패턴 ---")

# 기본값 딕셔너리 (collections.defaultdict)
from collections import defaultdict

# 리스트 기본값
dd_list = defaultdict(list)
dd_list["fruits"].append("apple")
dd_list["fruits"].append("banana")
dd_list["vegetables"].append("carrot")
print(f"defaultdict(list): {dict(dd_list)}")

# 정수 기본값 (카운팅)
dd_int = defaultdict(int)
for char in "hello world":
    dd_int[char] += 1
print(f"defaultdict(int) 문자 카운트: {dict(dd_int)}")

# Counter 사용
from collections import Counter

text = "hello world"
counter = Counter(text)
print(f"Counter('hello world'): {counter}")
print(f"가장 흔한 3개: {counter.most_common(3)}")

# OrderedDict (Python 3.7+에서는 일반 dict도 순서 보장)
from collections import OrderedDict

od = OrderedDict()
od["first"] = 1
od["second"] = 2
od["third"] = 3
print(f"OrderedDict: {od}")

# -----------------------------------------------------------------------------
# 2.10 딕셔너리 정렬
# -----------------------------------------------------------------------------
print("\n--- 2.10 딕셔너리 정렬 ---")

scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}

# 키로 정렬
sorted_by_key = dict(sorted(scores.items()))
print(f"키로 정렬: {sorted_by_key}")

# 값으로 정렬
sorted_by_value = dict(sorted(scores.items(), key=lambda x: x[1]))
print(f"값으로 정렬 (오름차순): {sorted_by_value}")

# 값으로 내림차순 정렬
sorted_by_value_desc = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(f"값으로 정렬 (내림차순): {sorted_by_value_desc}")


# =============================================================================
# 3. 튜플 vs 딕셔너리 비교
# =============================================================================

print("\n" + "=" * 60)
print("3. 튜플 vs 딕셔너리 비교")
print("=" * 60)

print("""
| 구분        | 튜플 (Tuple)           | 딕셔너리 (Dictionary)    |
|------------|------------------------|-------------------------|
| 기호        | ()                     | {}                      |
| 구조        | 순서가 있는 값들         | 키-값 쌍                 |
| 변경        | 불변 (Immutable)        | 가변 (Mutable)          |
| 접근        | 인덱스 (t[0])           | 키 (d["key"])           |
| 중복        | 값 중복 허용            | 키 중복 불가, 값 중복 허용 |
| 순서        | 유지됨                  | 유지됨 (Python 3.7+)    |
| 용도        | 고정 데이터, 함수 반환   | 매핑, 구조화된 데이터     |
| 해시        | 가능 (dict 키로 사용 가능)| 불가능                  |
""")


# =============================================================================
# 4. 실전 예제
# =============================================================================

print("=" * 60)
print("4. 실전 예제")
print("=" * 60)

# -----------------------------------------------------------------------------
# 4.1 학생 성적 관리 시스템
# -----------------------------------------------------------------------------
print("\n--- 4.1 학생 성적 관리 시스템 ---")

def create_student(name, *scores):
    """학생 정보 생성 (튜플로 과목 점수 받기)"""
    return {
        "name": name,
        "scores": scores,  # 튜플로 저장
        "average": sum(scores) / len(scores) if scores else 0
    }

def get_grade(average):
    """평균으로 학점 계산"""
    if average >= 90: return "A"
    elif average >= 80: return "B"
    elif average >= 70: return "C"
    elif average >= 60: return "D"
    else: return "F"

# 학생들 생성
students = {}
students["Kim"] = create_student("Kim", 85, 90, 78)
students["Lee"] = create_student("Lee", 92, 88, 95)
students["Park"] = create_student("Park", 76, 82, 79)

# 학점 추가
for name, info in students.items():
    info["grade"] = get_grade(info["average"])

# 결과 출력
print("학생 성적표:")
for name, info in students.items():
    scores_str = ", ".join(map(str, info["scores"]))
    print(f"  {name}: 점수=({scores_str}), 평균={info['average']:.1f}, 학점={info['grade']}")

# -----------------------------------------------------------------------------
# 4.2 좌표 시스템 (튜플 활용)
# -----------------------------------------------------------------------------
print("\n--- 4.2 좌표 시스템 (튜플 활용) ---")

def distance(point1, point2):
    """두 점 사이의 거리 계산"""
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# 좌표는 튜플로 표현 (불변이므로 적합)
cities = {
    (0, 0): "원점",
    (3, 4): "A도시",
    (6, 8): "B도시"
}

point_a = (3, 4)
point_b = (6, 8)
dist = distance(point_a, point_b)
print(f"{cities[point_a]}에서 {cities[point_b]}까지 거리: {dist:.2f}")

# -----------------------------------------------------------------------------
# 4.3 단어 빈도 분석
# -----------------------------------------------------------------------------
print("\n--- 4.3 단어 빈도 분석 ---")

text = "apple banana apple cherry banana apple"
words = text.split()

# 방법 1: 일반 딕셔너리
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(f"단어 빈도 (get 사용): {word_count}")

# 방법 2: setdefault
word_count2 = {}
for word in words:
    word_count2.setdefault(word, 0)
    word_count2[word] += 1
print(f"단어 빈도 (setdefault): {word_count2}")

# 방법 3: Counter
word_count3 = Counter(words)
print(f"단어 빈도 (Counter): {dict(word_count3)}")

# -----------------------------------------------------------------------------
# 4.4 그룹핑 (딕셔너리 + 튜플)
# -----------------------------------------------------------------------------
print("\n--- 4.4 그룹핑 ---")

# 학생들을 학년별로 그룹화
students_list = [
    ("Kim", 1, 85),
    ("Lee", 2, 92),
    ("Park", 1, 78),
    ("Choi", 2, 88),
    ("Jung", 1, 90)
]

# 학년별 그룹화
by_grade = defaultdict(list)
for name, grade, score in students_list:
    by_grade[grade].append((name, score))

print("학년별 학생:")
for grade, students in sorted(by_grade.items()):
    print(f"  {grade}학년: {students}")

print("\n프로그램 종료")
