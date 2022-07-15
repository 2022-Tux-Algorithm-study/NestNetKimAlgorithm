# 준희는,, 안귀엽나보다,, ㅠㅠ

n = int(input())
cute = [int(input()) for _ in range(n)]

n, y = 0, 0

for i in cute:
  if i == 1:
    y += 1
  else:
    n+= 1

if y > n:
  print('Junhee is cute!')

else:
  print('Junhee is not cute!')