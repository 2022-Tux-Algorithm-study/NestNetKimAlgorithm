# 플러그

import sys

n = int(sys.stdin.readline())
total = 0

for i in range(n):
  multi = int(sys.stdin.readline())
  total += multi

print(total-(n-1))

