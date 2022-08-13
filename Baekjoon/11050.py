# 이항 계수 1

import sys

n, k = map(int, sys.stdin.readline().split())
result = 1
a, b = 1, 1

for i in range(k):
  a *= (n-i)
  b *= (k-i)

print(a//b)


