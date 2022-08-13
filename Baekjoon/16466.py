# 콘서트
# 2차 티켓팅에서 양한이가 가질 수 있는 티켓 중 가장 작은 번호를 출력

import sys

n = int(sys.stdin.readline())
sold = list(map(int, sys.stdin.readline().split()))

ticket = [0] * 1000000
index = 0

for i in range(n):
  ticket[sold[i]-1] += 1

while(1):
  if ticket[index] == 0:
    print(index+1)
    break
  index += 1