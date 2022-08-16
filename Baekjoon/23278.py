# 영화 평가

import sys

n, l, h = map(int, sys.stdin.readline().split())

score = list(map(int, sys.stdin.readline().split()))

total = 0

score.sort()

for i in range(n):
  if i < l:
    continue
  elif len(score)-i <= h:
    continue
  else:
    total += score[i]
    
print(total/(n-(l+h)))