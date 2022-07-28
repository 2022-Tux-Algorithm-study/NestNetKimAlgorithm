n, m = map(int, input().split())
string = str(n)*n
list = list(string)

if len(string) > m:
  for i in range(0, m):
    print(list[i], end='')
else:
  print(string)
