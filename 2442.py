num = int(input());
k = 0
for i in range(0, num):
  for j in range(1, num-i):
    print(' ',end='')
  for j in range(0, k+1):
    print('*', end='')
  k += 2
  print('\n', end='')