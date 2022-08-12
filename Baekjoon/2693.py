# N번째 큰 수
# 배열 A가 주어졌을 때, N번째 큰 값을 출력하는 프로그램을 작성

import sys

t = int(sys.stdin.readline())

for i in range(t):
  a = list(map(int, sys.stdin.readline().split()))
  a.sort()
  print(a[7])