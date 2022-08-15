# 좌표 정렬하기

import sys

n = int(sys.stdin.readline())
math = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

math.sort()

for i in range(n):
  print(math[i][0], math[i][1])