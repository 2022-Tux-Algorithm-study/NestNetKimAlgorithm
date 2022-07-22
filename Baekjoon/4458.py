# 첫 글자를 대문자로

n = int(input())
sen = [list(input()) for _ in range(n)]

for i in range(0, n):
  sen[i][0] = sen[i][0].upper()
  for j in range(0, len(sen[i])):
    print(sen[i][j], end='')
  print('')