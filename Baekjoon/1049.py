n, m = map(int, input().split())

list = [list(map(int, input().split())) for _ in range(m)]

pack = n // 6 + 1
min = list[0][0] * pack

for i in range(0, m):

  for j in range(0, m):
    div = list[i][0] * (pack-1) + list[j][1] * (n-6*(pack-1))
    
    if min > div:
      min = div
  
  if min > list[i][0]*pack:
    min = list[i][0]*pack
    
  elif min > list[i][1]*n:
    min = list[i][1]*n

print(min)