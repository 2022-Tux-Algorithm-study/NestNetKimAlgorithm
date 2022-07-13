n = 5
score = list(int(input()) for _ in range(n))

total = 0

for a in score:
  if a < 40:
    total += 40
  else:
    total += a

print(total//n)