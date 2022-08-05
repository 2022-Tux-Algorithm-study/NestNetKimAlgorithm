# 10부제

n = int(input())
car = list(map(int, input().split()))
count = 0

for i in car:
  if i == n:
    count += 1

print(count)