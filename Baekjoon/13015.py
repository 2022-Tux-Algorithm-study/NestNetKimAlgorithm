# 별 찍기 - 23

n = int(input())

# 윗부분
for i in range(1, n):
  if i == 1:
    print('*' * n, end='')
  else:
    print(' ' * (i-1), end='')
    print('*' + ' ' * (n-2) + '*', end='')

  print(' ' * (2*(n-i)-1), end='')

  if i == 1:
    print('*' * n)
  else:
    print('*' + ' ' * (n-2) + '*')

# 센터
print(' ' * (n-1) + '*' + ' ' * (n-2) + '*' + ' ' * (n-2) + '*')

# 아랫부분
for i in range(1, n):
  if i == n-1:
    print('*' * n, end='')
  else:
    print(' ' * (n-i-1), end='')
    print('*' + ' ' * (n-2) + '*', end='')

  print(' ' * (2*i-1), end='')

  if i == n-1:
    print('*' * n)
  else:
    print('*' + ' ' * (n-2) + '*')
