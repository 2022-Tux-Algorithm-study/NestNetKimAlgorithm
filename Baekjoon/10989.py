# 수 정렬하기 3
# 메모리 제한으로 계수 정렬 사용해야함
# sort 사용 방식(수를 배열에 입력받는 방식)은 메모리 초과

import sys

n = int(sys.stdin.readline())
num = [0]*10000

# 입력 받은 숫자의 index에 +1
for i in range(n):
  a = int(sys.stdin.readline())
  num[a-1] += 1

# 입력받은 수의 개수만큼 출력 (0이 아닐경우)
for i in range(len(num)):
  if num[i] != 0:
    for j in range(num[i]):
      print(i+1)