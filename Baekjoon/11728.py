sa, sb = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


for i in range(0, sb):
  a.append(b[i])
a.sort()

for i in range(0, sa+sb):
  print(a[i], end=' ')