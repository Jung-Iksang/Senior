num = 100 
print(type(num))

result = 1
print(type(result))

# 진수 변환 예시
num = 11

# 10진수 → 다른 진수
print(bin(num))   # 2진수: 0b1011
print(oct(num))   # 8진수: 0o13
print(hex(num))   # 16진수: 0xb

# 다른 진수 → 10진수
print(int('1011', 2))   # 2진수 → 10진수: 11
print(int('13', 8))     # 8진수 → 10진수: 11
print(int('b', 16))     # 16진수 → 10진수: 11

a = 10
a += 10
a *= 2
print (a)


print(10==10)

