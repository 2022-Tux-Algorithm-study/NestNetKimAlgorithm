n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
pc = []

for i in range(0, n):
  a = data[i][0] % 10 
  
  if a == 1 or a == 5 or a == 6:
    pc.append(a)

  elif a == 2 or a == 8:
    b = data[i][1] % 4
    
    if b == 1:
      pc.append(a)
      
    elif b == 2:
      pc.append(4)

    elif b == 3:
      if a == 2: pc.append(8)
      else: pc.append(2)

    else:
      pc.append(6)

  elif a == 3 or a == 7:
    b = data[i][1] % 4
    
    if b == 1:
      pc.append(a)
      
    elif b == 2:
      pc.append(9)

    elif b == 3:
      if a == 3: pc.append(7)
      else: pc.append(3)

    else:
      pc.append(1)

  elif a == 4 or a == 9:
    b = data[i][1] % 2
    if b == 1:
      pc.append(a)
    else:
      if a == 4: pc.append(6)
      else: pc.append(1)

  else:
    pc.append(10)

for a in pc:
    print(a)