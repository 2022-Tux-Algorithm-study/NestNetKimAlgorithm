n = int(input())
list = [int(input()) for _ in range(n)]

for i in range(n):
  print('#'*list[i])
  mid = list[i] - 2
  
  for j in range(mid):
    print('#' + 'J'*mid +'# ')
  
  if list[i] != 1:
    print('#'*list[i])

  if i != n-1:
    print('')