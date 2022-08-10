# 수 정렬하기 2

# 참고: int(input()) 쓰면 시간 초과 뜸 ㅠ

import sys
n = int(sys.stdin.readline())
num = [int(sys.stdin.readline()) for _ in range(n)]

num.sort()

for i in num:
  print(i)