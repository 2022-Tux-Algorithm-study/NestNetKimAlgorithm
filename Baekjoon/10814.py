# 나이순 정렬

import sys

n = int(sys.stdin.readline())
mem = []

for i in range(n):
  age, name = sys.stdin.readline().split()
  mem.append([int(age), name])

mem = sorted(mem, key = lambda x : x[0])

for i in range(n):
  print(mem[i][0], mem[i][1])