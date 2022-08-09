# 이진수

t = int(input())

for i in range(t):
  n = int(input())
  n = format(n, 'b')
  n = str(n)
  for i in range(len(n)):
    if n[len(n)-i-1] == '1':
      print(i, end=' ')