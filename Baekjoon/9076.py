num = int(input())
arr = []

for i in range(num):    
	arr.append(list(map(int, input().split())))

for i in range(num):
  total = 0
  kin = 0
  arr[i].sort()
  kin = arr[i][3] - arr[i][1]

  if kin >= 4:
    print('KIN')

  else:
    for k in range(1, 4):
      total += arr[i][k]
    print(total)