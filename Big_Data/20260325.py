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

# =============================================================================
# 5. 세트 (Set) - 중복 없는 순서 없는 컬렉션
# =============================================================================

print("\n" + "=" * 60)
print("5. 세트 (Set)")
print("=" * 60)

# -----------------------------------------------------------------------------
# 5.1 세트 생성
# -----------------------------------------------------------------------------
print("\n--- 5.1 세트 생성 ---")

s1 = {1, 2, 3}                  # 기본 생성
s2 = set()                       # 빈 세트 ({}는 딕셔너리!)
s3 = set([1, 2, 2, 3, 3, 3])    # 리스트 -> 세트 (중복 제거)
s4 = set("hello")                # 문자열 -> 세트
s5 = set(range(5))               # range -> 세트

print(f"s1 = {{1, 2, 3}}: {s1}")
print(f"s2 = set(): {s2}")
print(f"s3 = set([1,2,2,3,3,3]): {s3}")  # 중복 제거됨
print(f"s4 = set('hello'): {s4}")         # 순서 없음
print(f"s5 = set(range(5)): {s5}")

# 주의: 빈 세트는 set()으로만 생성!
empty_dict = {}
empty_set = set()
print(f"{{}}의 타입: {type(empty_dict)}")
print(f"set()의 타입: {type(empty_set)}")

# -----------------------------------------------------------------------------
# 5.2 세트의 특징
# -----------------------------------------------------------------------------
print("\n--- 5.2 세트의 특징 ---")

# 1. 중복 불가
s = {1, 1, 2, 2, 3}
print(f"{{1, 1, 2, 2, 3}}: {s}")  # {1, 2, 3}

# 2. 순서 없음 (인덱싱 불가)
print("세트는 인덱싱 불가! s[0] -> TypeError")
# s[0]  # TypeError

# 3. 가변(mutable) - 요소 추가/삭제 가능
s = {1, 2, 3}
s.add(4)
print(f"add(4) 후: {s}")

# 4. 요소는 불변(immutable)이어야 함
# {[1, 2]}  # TypeError: 리스트는 불가
s = {(1, 2), (3, 4)}  # 튜플은 가능
print(f"튜플 요소 세트: {s}")

# -----------------------------------------------------------------------------
# 5.3 세트 요소 추가/삭제
# -----------------------------------------------------------------------------
print("\n--- 5.3 세트 요소 추가/삭제 ---")

s = {1, 2, 3}
print(f"원본: {s}")

# 추가
s.add(4)
print(f"add(4): {s}")

s.add(4)  # 이미 있으면 무시
print(f"add(4) 다시: {s}")

# 여러 개 추가
s.update([5, 6, 7])
print(f"update([5, 6, 7]): {s}")

s.update({8, 9}, [10])  # 여러 이터러블 가능
print(f"update({{8, 9}}, [10]): {s}")

# 삭제
s.remove(10)  # 없으면 KeyError
print(f"remove(10): {s}")

s.discard(100)  # 없어도 에러 안남
print(f"discard(100): {s}")

popped = s.pop()  # 임의의 요소 제거 (순서 없으므로)
print(f"pop(): {popped}, 세트: {s}")

s.clear()  # 전체 삭제
print(f"clear(): {s}")

# -----------------------------------------------------------------------------
# 5.4 세트 연산 (집합 연산)
# -----------------------------------------------------------------------------
print("\n--- 5.4 세트 연산 (집합 연산) ---")

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"a = {a}")
print(f"b = {b}")

# 합집합 (Union)
print(f"\n[합집합 - Union]")
print(f"a | b: {a | b}")
print(f"a.union(b): {a.union(b)}")

# 교집합 (Intersection)
print(f"\n[교집합 - Intersection]")
print(f"a & b: {a & b}")
print(f"a.intersection(b): {a.intersection(b)}")

# 차집합 (Difference)
print(f"\n[차집합 - Difference]")
print(f"a - b: {a - b}")  # a에만 있는 것
print(f"b - a: {b - a}")  # b에만 있는 것
print(f"a.difference(b): {a.difference(b)}")

# 대칭 차집합 (Symmetric Difference) - 둘 중 하나에만 있는 것
print(f"\n[대칭 차집합 - Symmetric Difference]")
print(f"a ^ b: {a ^ b}")
print(f"a.symmetric_difference(b): {a.symmetric_difference(b)}")

# -----------------------------------------------------------------------------
# 5.5 세트 연산 (제자리 연산)
# -----------------------------------------------------------------------------
print("\n--- 5.5 세트 연산 (제자리 연산) ---")

# |= (합집합 업데이트)
s = {1, 2, 3}
s |= {4, 5}
print(f"s |= {{4, 5}}: {s}")

# &= (교집합 업데이트)
s = {1, 2, 3, 4, 5}
s &= {2, 3, 4}
print(f"s &= {{2, 3, 4}}: {s}")

# -= (차집합 업데이트)
s = {1, 2, 3, 4, 5}
s -= {4, 5}
print(f"s -= {{4, 5}}: {s}")

# ^= (대칭 차집합 업데이트)
s = {1, 2, 3}
s ^= {2, 3, 4}
print(f"s ^= {{2, 3, 4}}: {s}")

# 메서드 버전
s = {1, 2, 3}
s.update({4, 5})           # |=
print(f"update({{4, 5}}): {s}")

s.intersection_update({2, 3, 4, 5})  # &=
print(f"intersection_update({{2, 3, 4, 5}}): {s}")

s = {1, 2, 3, 4, 5}
s.difference_update({4, 5})  # -=
print(f"difference_update({{4, 5}}): {s}")

s.symmetric_difference_update({2, 3, 6})  # ^=
print(f"symmetric_difference_update({{2, 3, 6}}): {s}")

# -----------------------------------------------------------------------------
# 5.6 세트 관계 연산
# -----------------------------------------------------------------------------
print("\n--- 5.6 세트 관계 연산 ---")

a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
c = {1, 2, 3}
d = {6, 7, 8}

print(f"a = {a}, b = {b}, c = {c}, d = {d}")

# 부분집합 (Subset)
print(f"\na <= b (a는 b의 부분집합?): {a <= b}")
print(f"a.issubset(b): {a.issubset(b)}")

# 진부분집합 (Proper Subset)
print(f"a < b (a는 b의 진부분집합?): {a < b}")
print(f"a < c: {a < c}")  # 같으면 False

# 상위집합 (Superset)
print(f"\nb >= a (b는 a의 상위집합?): {b >= a}")
print(f"b.issuperset(a): {b.issuperset(a)}")

# 진상위집합 (Proper Superset)
print(f"b > a: {b > a}")

# 서로소 (Disjoint) - 교집합이 없음
print(f"\na.isdisjoint(d) (서로소?): {a.isdisjoint(d)}")
print(f"a.isdisjoint(b): {a.isdisjoint(b)}")

# 동등
print(f"\na == c: {a == c}")

# -----------------------------------------------------------------------------
# 5.7 세트 메서드 정리
# -----------------------------------------------------------------------------
print("\n--- 5.7 세트 메서드 정리 ---")

s = {3, 1, 4, 1, 5, 9, 2, 6}
print(f"세트: {s}")
print(f"len(s): {len(s)}")
print(f"max(s): {max(s)}")
print(f"min(s): {min(s)}")
print(f"sum(s): {sum(s)}")
print(f"sorted(s): {sorted(s)}")  # 리스트 반환
print(f"3 in s: {3 in s}")
print(f"10 in s: {10 in s}")

# copy
s2 = s.copy()
print(f"s.copy(): {s2}")

# -----------------------------------------------------------------------------
# 5.8 frozenset (불변 세트)
# -----------------------------------------------------------------------------
print("\n--- 5.8 frozenset (불변 세트) ---")

# frozenset: 불변(immutable) 세트
fs = frozenset([1, 2, 3])
print(f"frozenset([1, 2, 3]): {fs}")
print(f"타입: {type(fs)}")

# 수정 불가
# fs.add(4)  # AttributeError

# 집합 연산은 가능
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
print(f"fs1 | fs2: {fs1 | fs2}")
print(f"fs1 & fs2: {fs1 & fs2}")

# 딕셔너리 키나 세트의 요소로 사용 가능
d = {frozenset([1, 2]): "값"}
print(f"frozenset을 딕셔너리 키로: {d}")

s = {frozenset([1, 2]), frozenset([3, 4])}
print(f"frozenset을 세트 요소로: {s}")

# -----------------------------------------------------------------------------
# 5.9 세트 활용 예시
# -----------------------------------------------------------------------------
print("\n--- 5.9 세트 활용 예시 ---")

# 1. 중복 제거
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = list(set(numbers))
print(f"중복 제거: {numbers} -> {unique}")

# 2. 멤버십 테스트 (리스트보다 빠름)
large_set = set(range(100000))
print(f"99999 in large_set: {99999 in large_set}")

# 3. 공통 요소 찾기
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = set(list1) & set(list2)
print(f"공통 요소: {common}")

# 4. 고유 요소 찾기
all_items = set(list1) | set(list2)
print(f"모든 고유 요소: {all_items}")

# 5. 차이 찾기
only_in_list1 = set(list1) - set(list2)
print(f"list1에만 있는 요소: {only_in_list1}")

# 6. 문자열에서 고유 문자
text = "programming"
unique_chars = set(text)
print(f"'{text}'의 고유 문자: {unique_chars}")
print(f"고유 문자 수: {len(unique_chars)}")


# =============================================================================
# 6. 컬렉션 내포 (Comprehension) - 리스트, 딕셔너리, 세트, 제너레이터
# =============================================================================

print("\n" + "=" * 60)
print("6. 컬렉션 내포 (Comprehension)")
print("=" * 60)

# -----------------------------------------------------------------------------
# 6.1 리스트 컴프리헨션 (List Comprehension)
# -----------------------------------------------------------------------------
print("\n--- 6.1 리스트 컴프리헨션 ---")

# 기본 문법: [표현식 for 변수 in 반복가능객체]

# 기본 형태
squares = [x**2 for x in range(1, 6)]
print(f"[x**2 for x in range(1, 6)]: {squares}")

# 기존 for문과 비교
squares_loop = []
for x in range(1, 6):
    squares_loop.append(x**2)
print(f"for문 결과: {squares_loop}")

# 표현식에 함수 사용
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"대문자 변환: {upper_words}")

# 표현식에 메서드 체이닝
stripped = [s.strip().lower() for s in ["  Hello  ", " WORLD ", "  PyThOn  "]]
print(f"공백 제거 + 소문자: {stripped}")

# -----------------------------------------------------------------------------
# 6.2 조건부 리스트 컴프리헨션
# -----------------------------------------------------------------------------
print("\n--- 6.2 조건부 리스트 컴프리헨션 ---")

# if 조건 (필터링)
# 문법: [표현식 for 변수 in 반복가능객체 if 조건]
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"짝수만: {evens}")

# 여러 조건 (and)
result = [x for x in range(1, 31) if x % 2 == 0 if x % 3 == 0]
print(f"2와 3의 배수: {result}")

# 위와 동일
result2 = [x for x in range(1, 31) if x % 2 == 0 and x % 3 == 0]
print(f"2와 3의 배수 (and): {result2}")

# if-else (삼항 연산자)
# 문법: [참값 if 조건 else 거짓값 for 변수 in 반복가능객체]
labels = ["짝수" if x % 2 == 0 else "홀수" for x in range(1, 6)]
print(f"홀짝 라벨: {labels}")

# 값 변환
abs_values = [x if x >= 0 else -x for x in [-3, -1, 0, 2, 5]]
print(f"절대값: {abs_values}")

# if-elif-else (중첩 삼항 연산자)
grades = [90, 75, 60, 45, 85]
labels = ["A" if g >= 90 else "B" if g >= 80 else "C" if g >= 70 else "D" if g >= 60 else "F" for g in grades]
print(f"학점: {grades} -> {labels}")

# -----------------------------------------------------------------------------
# 6.3 중첩 리스트 컴프리헨션
# -----------------------------------------------------------------------------
print("\n--- 6.3 중첩 리스트 컴프리헨션 ---")

# 2중 for문
# 문법: [표현식 for 변수1 in 반복가능객체1 for 변수2 in 반복가능객체2]
pairs = [(x, y) for x in [1, 2, 3] for y in ['a', 'b']]
print(f"모든 조합: {pairs}")

# 기존 for문과 비교
pairs_loop = []
for x in [1, 2, 3]:
    for y in ['a', 'b']:
        pairs_loop.append((x, y))
print(f"for문 결과: {pairs_loop}")

# 구구단
gugudan = [f"{i}x{j}={i*j}" for i in range(2, 4) for j in range(1, 4)]
print(f"구구단: {gugudan}")

# 2차원 리스트 평탄화 (flatten)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix for x in row]
print(f"평탄화: {matrix} -> {flattened}")

# 2차원 리스트 생성
matrix = [[i * 3 + j for j in range(1, 4)] for i in range(3)]
print(f"2차원 리스트 생성: {matrix}")

# 전치 행렬 (transpose)
original = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in original] for i in range(3)]
print(f"원본: {original}")
print(f"전치: {transposed}")

# 조건부 중첩
filtered_pairs = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]
print(f"x != y인 쌍: {filtered_pairs}")

# -----------------------------------------------------------------------------
# 6.4 딕셔너리 컴프리헨션 (Dictionary Comprehension)
# -----------------------------------------------------------------------------
print("\n--- 6.4 딕셔너리 컴프리헨션 ---")

# 기본 문법: {키표현식: 값표현식 for 변수 in 반복가능객체}

# 기본 형태
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"{{x: x**2 for x in range(1, 6)}}: {squares_dict}")

# 조건부
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"짝수 제곱: {even_squares}")

# 두 리스트로 딕셔너리 생성
keys = ["name", "age", "city"]
values = ["Alice", 25, "Seoul"]
person = {k: v for k, v in zip(keys, values)}
print(f"zip으로 딕셔너리: {person}")

# 키-값 교환
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(f"키-값 교환: {original} -> {reversed_dict}")

# 값 변환
prices = {"apple": 100, "banana": 200, "orange": 150}
discounted = {k: v * 0.9 for k, v in prices.items()}
print(f"10% 할인: {prices} -> {discounted}")

# 조건부 값
numbers = [1, 2, 3, 4, 5]
categorized = {n: ("짝수" if n % 2 == 0 else "홀수") for n in numbers}
print(f"숫자 분류: {categorized}")

# 문자열 처리
words = ["Hello", "World", "Python"]
word_lengths = {word: len(word) for word in words}
print(f"단어 길이: {word_lengths}")

# 중첩 딕셔너리 컴프리헨션
matrix_dict = {i: {j: i * j for j in range(1, 4)} for i in range(1, 4)}
print(f"중첩 딕셔너리: {matrix_dict}")

# enumerate 활용
fruits = ["apple", "banana", "cherry"]
indexed = {i: fruit for i, fruit in enumerate(fruits)}
print(f"인덱스 딕셔너리: {indexed}")

# 조건부 키 필터링
scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65}
passed = {name: score for name, score in scores.items() if score >= 75}
print(f"75점 이상: {passed}")

# -----------------------------------------------------------------------------
# 6.5 세트 컴프리헨션 (Set Comprehension)
# -----------------------------------------------------------------------------
print("\n--- 6.5 세트 컴프리헨션 ---")

# 기본 문법: {표현식 for 변수 in 반복가능객체}

# 기본 형태
squares_set = {x**2 for x in range(-3, 4)}
print(f"{{x**2 for x in range(-3, 4)}}: {squares_set}")  # 중복 자동 제거

# 조건부
evens_set = {x for x in range(1, 11) if x % 2 == 0}
print(f"짝수 세트: {evens_set}")

# 문자열에서 모음만
text = "Hello World Python"
vowels = {char.lower() for char in text if char.lower() in 'aeiou'}
print(f"'{text}'의 모음: {vowels}")

# 리스트에서 중복 제거 + 변환
numbers = [1, -2, 2, -3, 3, -1]
abs_set = {abs(x) for x in numbers}
print(f"절대값 세트: {abs_set}")

# 단어 길이 세트
words = ["apple", "banana", "cherry", "date", "fig"]
lengths = {len(word) for word in words}
print(f"단어 길이 종류: {lengths}")

# 두 리스트의 공통 요소
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = {x for x in list1 if x in list2}
print(f"공통 요소: {common}")

# -----------------------------------------------------------------------------
# 6.6 제너레이터 표현식 (Generator Expression)
# -----------------------------------------------------------------------------
print("\n--- 6.6 제너레이터 표현식 ---")

# 기본 문법: (표현식 for 변수 in 반복가능객체)
# 리스트 컴프리헨션과 같지만 () 사용

# 기본 형태
gen = (x**2 for x in range(1, 6))
print(f"제너레이터 객체: {gen}")
print(f"타입: {type(gen)}")

# 값 가져오기
print(f"next(gen): {next(gen)}")
print(f"next(gen): {next(gen)}")

# 리스트로 변환
gen = (x**2 for x in range(1, 6))
print(f"list(gen): {list(gen)}")

# 함수에 직접 전달 (괄호 생략 가능)
total = sum(x**2 for x in range(1, 6))
print(f"sum(x**2 for x in range(1, 6)): {total}")

max_val = max(x**2 for x in range(1, 6))
print(f"max(x**2 for x in range(1, 6)): {max_val}")

# any, all과 함께
numbers = [2, 4, 6, 8, 10]
all_even = all(x % 2 == 0 for x in numbers)
any_over_5 = any(x > 5 for x in numbers)
print(f"모두 짝수?: {all_even}")
print(f"5 초과 있음?: {any_over_5}")

# 조건부
even_squares = (x**2 for x in range(1, 11) if x % 2 == 0)
print(f"짝수 제곱: {list(even_squares)}")

# 메모리 효율성 비교
import sys
list_comp = [x for x in range(10000)]
gen_exp = (x for x in range(10000))
print(f"\n[메모리 비교]")
print(f"리스트 크기: {sys.getsizeof(list_comp)} bytes")
print(f"제너레이터 크기: {sys.getsizeof(gen_exp)} bytes")

# -----------------------------------------------------------------------------
# 6.7 컴프리헨션 비교 정리
# -----------------------------------------------------------------------------
print("\n--- 6.7 컴프리헨션 비교 정리 ---")

print("""
| 타입       | 문법                              | 결과 타입    | 특징                    |
|-----------|----------------------------------|-------------|------------------------|
| 리스트     | [expr for x in iterable]        | list        | 순서 유지, 인덱싱 가능    |
| 딕셔너리   | {k: v for x in iterable}        | dict        | 키-값 쌍                |
| 세트      | {expr for x in iterable}         | set         | 중복 제거, 순서 없음     |
| 제너레이터 | (expr for x in iterable)         | generator   | 지연 평가, 메모리 효율   |
""")

# 같은 데이터로 비교
data = [1, 2, 2, 3, 3, 3]

list_result = [x**2 for x in data]
set_result = {x**2 for x in data}
dict_result = {x: x**2 for x in data}
gen_result = (x**2 for x in data)

print(f"원본 데이터: {data}")
print(f"리스트 컴프리헨션: {list_result}")
print(f"세트 컴프리헨션: {set_result}")
print(f"딕셔너리 컴프리헨션: {dict_result}")
print(f"제너레이터 표현식: {list(gen_result)}")

# -----------------------------------------------------------------------------
# 6.8 고급 컴프리헨션 패턴
# -----------------------------------------------------------------------------
print("\n--- 6.8 고급 컴프리헨션 패턴 ---")

# 1. walrus 연산자 (:=) 사용 (Python 3.8+)
# 표현식 내에서 변수 할당
results = [y for x in range(5) if (y := x**2) > 5]
print(f"walrus 연산자: {results}")

# 2. 복잡한 조건과 변환
data = ["  Alice  ", "Bob", "", "  Charlie  ", None, "David"]
cleaned = [name.strip() for name in data if name and name.strip()]
print(f"정제된 이름: {cleaned}")

# 3. 딕셔너리에서 필터링 후 변환
students = {
    "Alice": {"score": 85, "grade": "B"},
    "Bob": {"score": 92, "grade": "A"},
    "Charlie": {"score": 78, "grade": "C"}
}
high_scorers = {name: info["score"] for name, info in students.items() if info["score"] >= 80}
print(f"80점 이상: {high_scorers}")

# 4. 여러 반복 가능 객체 조합
names = ["Alice", "Bob"]
ages = [25, 30]
cities = ["Seoul", "Busan"]
people = [{"name": n, "age": a, "city": c} for n, a, c in zip(names, ages, cities)]
print(f"zip 조합: {people}")

# 5. 함수 호출 결과로 컴프리헨션
def process(x):
    return x * 2 if x % 2 == 0 else x * 3

processed = [process(x) for x in range(1, 6)]
print(f"함수 적용: {processed}")

# 6. 문자열 처리
sentence = "The Quick Brown Fox"
word_info = {word: (len(word), word.lower()) for word in sentence.split()}
print(f"단어 정보: {word_info}")


# =============================================================================
# 7. 컬렉션 타입 비교 총정리
# =============================================================================

print("\n" + "=" * 60)
print("7. 컬렉션 타입 비교 총정리")
print("=" * 60)

print("""
| 타입        | 기호  | 순서 | 변경 | 중복 | 인덱싱 | 용도                      |
|------------|------|------|------|------|--------|--------------------------|
| 리스트      | []   | O    | O    | O    | O      | 순서 있는 가변 데이터       |
| 튜플        | ()   | O    | X    | O    | O      | 순서 있는 불변 데이터       |
| 딕셔너리    | {}   | O*   | O    | 키X  | 키     | 키-값 매핑                 |
| 세트        | {}   | X    | O    | X    | X      | 중복 없는 집합 연산         |
| frozenset  | -    | X    | X    | X    | X      | 불변 집합                  |

* Python 3.7+에서 딕셔너리 삽입 순서 유지
""")

# 실제 예시
print("--- 실제 사용 예시 ---")

# 리스트: 순서가 중요한 데이터
shopping_list = ["사과", "바나나", "우유"]
print(f"리스트 (쇼핑 목록): {shopping_list}")

# 튜플: 변경되면 안 되는 데이터
coordinates = (37.5, 127.0)
print(f"튜플 (좌표): {coordinates}")

# 딕셔너리: 키로 값을 찾는 데이터
person = {"name": "Alice", "age": 25}
print(f"딕셔너리 (개인정보): {person}")

# 세트: 중복 없는 집합
unique_visitors = {"Alice", "Bob", "Alice", "Charlie"}
print(f"세트 (방문자): {unique_visitors}")

print("\n프로그램 종료")
