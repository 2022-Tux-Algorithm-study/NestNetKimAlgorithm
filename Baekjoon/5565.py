cost = [int(input()) for _ in range(10)]
total = cost[0]

for i in cost:
  if i == total:
    continue
  else:
    total -= i

print(total)