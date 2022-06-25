n = 7
total = 0
min = 10000
list = [int(input()) for _ in range(n)]

for i in range(n):
  if list[i]%2 != 0:
    total += list[i]
    if min > list[i]:
      min = list[i]

if total == 0:
  print(-1)
else:
  print(total)
  print(min)