# 수열의 변화

n, k = map(int, input().split())

a = list(map(int, input().split(',')))

for i in range(k):
  for j in range(len(a)-1):
    a[j] = a[j+1] - a[j]
    if j == len(a)-2:
      a.pop(len(a)-1)

for i in range(len(a)):
  if i != len(a)-1:
    print(a[i], end=',')
  else:
    print(a[i])
