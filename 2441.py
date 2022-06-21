num = int(input());

for i in range(0, num):
  for j in range(0, i):
    print(' ', end='')
  for j in range(num-i, 0, -1):
    print('*', end='')
  print('\n', end='')