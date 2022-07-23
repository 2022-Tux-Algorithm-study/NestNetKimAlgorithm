# 수 뒤집기

num = int(input())
for i in range(num):
  n = input()
  n2 = ''.join(reversed(n))

  total = int(n) + int(n2)
  total = list(str(total))

  if total == total[::-1]:
    print('YES')
  else:
    print('NO')