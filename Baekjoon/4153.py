ans = []

while(1):
  tri = list(map(int, input().split()))
  tri.sort()
  
  if tri[0] == 0:
    break
    
  else:
    
    if tri[0]**2 + tri[1]**2 == tri[2]**2:
      ans.append('right')
      
    else:
      ans.append('wrong')

for a in ans:
  print(a)