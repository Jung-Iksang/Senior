# ===== Python 리스트 완벽 정리 =====

# ===== 1. 리스트 생성 =====
list1 = []                      # 빈 리스트
list2 = [1, 2, 3, 4, 5]         # 숫자 리스트
list3 = ["a", "b", "c"]         # 문자열 리스트
list4 = [1, "hello", 3.14, True] # 혼합 리스트
list5 = [[1, 2], [3, 4]]        # 2차원 리스트
list6 = list(range(5))          # [0, 1, 2, 3, 4]
list7 = list("hello")           # ['h', 'e', 'l', 'l', 'o']

# ===== 2. 인덱싱 (접근) =====
nums = [10, 20, 30, 40, 50]
print(nums[0])    # 10 (첫 번째)
print(nums[-1])   # 50 (마지막)
print(nums[2])    # 30 (세 번째)
print(nums[-2])   # 40 (뒤에서 두 번째)

# ===== 3. 슬라이싱 =====
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[2:5])    # [2, 3, 4] (2~4번 인덱스)
print(nums[:3])     # [0, 1, 2] (처음~2번)
print(nums[7:])     # [7, 8, 9] (7번~끝)
print(nums[::2])    # [0, 2, 4, 6, 8] (짝수 인덱스)
print(nums[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (역순)
print(nums[1:8:2])  # [1, 3, 5, 7] (1~7, 2칸씩)

# ===== 4. 요소 추가 =====
fruits = ["apple", "banana"]
fruits.append("cherry")          # 끝에 추가: ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")       # 1번 위치에 삽입: ['apple', 'orange', 'banana', 'cherry']
fruits.extend(["grape", "melon"]) # 여러 개 추가
print(fruits)

# ===== 5. 요소 삭제 =====
nums = [1, 2, 3, 4, 5, 3]
nums.remove(3)       # 값 3 삭제 (첫 번째만): [1, 2, 4, 5, 3]
popped = nums.pop()  # 마지막 요소 꺼내기: 3, 리스트는 [1, 2, 4, 5]
popped2 = nums.pop(1) # 1번 인덱스 꺼내기: 2
del nums[0]          # 0번 인덱스 삭제
nums.clear()         # 전체 삭제
print(nums)

# ===== 6. 검색 =====
animals = ["cat", "dog", "bird", "dog"]
print("dog" in animals)        # True (존재 여부)
print("fish" not in animals)   # True (없음 여부)
print(animals.index("dog"))    # 1 (첫 번째 위치)
print(animals.count("dog"))    # 2 (개수)

# ===== 7. 정렬 =====
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()                    # 오름차순 정렬 (원본 변경)
print(nums)                    # [1, 1, 2, 3, 4, 5, 6, 9]
nums.sort(reverse=True)        # 내림차순 정렬
print(nums)                    # [9, 6, 5, 4, 3, 2, 1, 1]

nums2 = [3, 1, 4, 1, 5]
sorted_nums = sorted(nums2)    # 새 리스트 반환 (원본 유지)
print(sorted_nums)             # [1, 1, 3, 4, 5]
print(nums2)                   # [3, 1, 4, 1, 5] (원본 그대로)

# ===== 8. 뒤집기 =====
nums = [1, 2, 3, 4, 5]
nums.reverse()                 # 원본 뒤집기
print(nums)                    # [5, 4, 3, 2, 1]
print(nums[::-1])              # 슬라이싱으로 뒤집기 (원본 유지)

# ===== 9. 복사 =====
original = [1, 2, 3]
copy1 = original.copy()        # 얕은 복사
copy2 = list(original)         # 얕은 복사
copy3 = original[:]            # 슬라이싱 복사

import copy
deep_copy = copy.deepcopy([[1, 2], [3, 4]])  # 깊은 복사 (2차원 이상)

# ===== 10. 리스트 연산 =====
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)      # [1, 2, 3, 4, 5, 6] (연결)
print(a * 3)      # [1, 2, 3, 1, 2, 3, 1, 2, 3] (반복)
print(len(a))     # 3 (길이)
print(min(a))     # 1 (최소값)
print(max(a))     # 3 (최대값)
print(sum(a))     # 6 (합계)

# ===== 11. 리스트 컴프리헨션 =====
# 기본
squares = [x**2 for x in range(5)]           # [0, 1, 4, 9, 16]

# 조건 포함
evens = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]

# 변환
words = ["hello", "world"]
upper_words = [w.upper() for w in words]     # ['HELLO', 'WORLD']

# 중첩
matrix = [[i*3+j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

# 2차원 펼치기
flat = [x for row in matrix for x in row]   # [0, 1, 2, 3, 4, 5, 6, 7, 8]

print(squares)
print(evens)
print(upper_words)
print(matrix)
print(flat)

# ===== 12. 2차원 리스트 =====
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])      # [1, 2, 3] (첫 번째 행)
print(matrix[1][2])   # 6 (2행 3열)
print(matrix[0][0])   # 1 (1행 1열)

# 행 순회
for row in matrix:
    print(row)

# 모든 요소 순회
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

# ===== 13. enumerate (인덱스와 값 동시 접근) =====
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# ===== 14. zip (여러 리스트 동시 순회) =====
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name}: {age}")
# Alice: 25
# Bob: 30
# Charlie: 35

# ===== 15. map, filter =====
nums = [1, 2, 3, 4, 5]

# map: 모든 요소에 함수 적용
squared = list(map(lambda x: x**2, nums))    # [1, 4, 9, 16, 25]

# filter: 조건에 맞는 요소만
evens = list(filter(lambda x: x % 2 == 0, nums))  # [2, 4]

print(squared)
print(evens)

# ===== 16. 리스트 메서드 정리 =====
"""
| 메서드      | 설명                    | 예시                    |
|------------|------------------------|------------------------|
| append()   | 끝에 요소 추가           | lst.append(x)          |
| insert()   | 특정 위치에 삽입         | lst.insert(i, x)       |
| extend()   | 여러 요소 추가           | lst.extend([1,2])      |
| remove()   | 값으로 삭제 (첫 번째)     | lst.remove(x)          |
| pop()      | 인덱스로 꺼내기          | lst.pop(i)             |
| clear()    | 전체 삭제               | lst.clear()            |
| index()    | 값의 인덱스 찾기         | lst.index(x)           |
| count()    | 값의 개수               | lst.count(x)           |
| sort()     | 정렬 (원본 변경)         | lst.sort()             |
| reverse()  | 뒤집기 (원본 변경)       | lst.reverse()          |
| copy()     | 얕은 복사               | lst.copy()             |
"""
