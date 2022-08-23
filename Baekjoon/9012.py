# 괄호

n = int(input())
left = '('
right = ')'

for i in range(n):
  count_l, count_r = 0, 0
  vps = input()

  for i in range(len(vps)):
    if vps[i] == left:
      count_l += 1
    elif vps[i] == right:
      count_r += 1
    if count_l == count_r:
      count_l, count_r = 0, 0
    elif count_l == 0 and count_r != 0:
      break

  if count_l != count_r:
    print('NO')
  else:
    print('YES')