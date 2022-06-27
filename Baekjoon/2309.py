n = 9
h = [int(input()) for _ in range(n)]
total = 0

for i in range(n):
  total += h[i]

for i in range(n):
  for k in range(i+1, n):
    sum = h[i] + h[k]
    find = total - sum
    
    if find == 100:
      h.pop(i)
      h.pop(k-1)
      break
      
  if len(h) == 7:
    break

h.sort()   
for i in range(len(h)):
  print(h[i])