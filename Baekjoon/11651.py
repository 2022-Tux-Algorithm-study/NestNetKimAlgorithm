# 좌표 정렬하기 2
# y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬

import sys

n = int(sys.stdin.readline())
co = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

co.sort()
co.sort(key=lambda x:x[1])

for i in co:
  print(i[0], i[1])