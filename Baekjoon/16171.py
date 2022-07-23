# 나는 친구가 적다 (Small)

note = list(input())
need = input()
num = '0123456789'
new = []

for a in note:
  if a not in num:
    new.append(a)
  
new = ''.join(new)

if need in new:
  print(1)
else:
  print(0)
