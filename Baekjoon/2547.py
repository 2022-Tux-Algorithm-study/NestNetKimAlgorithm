n = int(input())
ans = []

for i in range(n):
  input()
  stu = int(input())
  total = 0
  for j in range(stu):
    candy = int(input())
    total += candy
  if total % stu == 0:
    ans.append('YES')
  else:
    ans.append('NO')

for a in ans:
  print(a)