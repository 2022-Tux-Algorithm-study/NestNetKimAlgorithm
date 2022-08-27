# 반지

import sys

find = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
count = 0

for i in range(n):
  ring = sys.stdin.readline().strip()
  ring += ring
  
  if find in ring:
    count += 1

print(count)



## 왜 틀렸지 이해가 안되넴~

#import sys

# find = sys.stdin.readline().strip()
# n = int(sys.stdin.readline())
# count = 0

# for i in range(n):
#   ring = sys.stdin.readline().strip()
#   l = len(find)
  
#   if find in ring:
#     count += 1
    
#   for j in range(1, l):    
#     if ring[:j] == find[l-j:] and ring[10-(l-j):] == find[:l-j]:
#       count += 1

# print(count)