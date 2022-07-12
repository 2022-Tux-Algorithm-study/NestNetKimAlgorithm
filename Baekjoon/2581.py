m = int(input())
n = int(input())
total = 0

for i in range(m, n+1):
  result = True
  if i == 1:
    continue
  
  for j in range(2, i):
    
    if i%j == 0:
      result = False
      break
    
  if result == True:
    if total == 0:
      min = i
    total += i

if total == 0:
  print(-1)
else:
  print(total)
  print(min)