# 공백 없는 A+B

n = int(input())
a = n//10
b = n%10

if a > 10:
  a //= 10
  b = 10

print(a+b)