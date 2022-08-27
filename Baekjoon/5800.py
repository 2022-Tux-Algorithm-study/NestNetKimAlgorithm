# 성적 통계

import sys

n = int(sys.stdin.readline())
stu = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):  
  gap = 0
  
  score = stu[i][1:]
  score.sort()
  
  for j in range(stu[i][0]-1):
    if gap < score[j+1] - score[j]:
      gap = score[j+1] - score[j]

  print('Class', i+1)
  print('Max ' + str(max(stu[i][1:])) + ', Min ' + str(min(stu[i][1:])) + ', Largest gap', gap)